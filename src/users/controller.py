from database_handler import DbConn
from flask import jsonify
from werkzeug.security import check_password_hash, generate_password_hash
from flask_jwt_extended import create_access_token
from datetime import datetime

class UserController:

    """User controller interfaces with the database."""

    def __init__(self):
        """Initializes the user controller class."""
        conn = DbConn()
        self.cur = conn.create_connection()
        conn.create_users_table()

    def create_user(self, username, password, email, firstname, lastname, role):
        """Creates a user.
        
        Arguments:
          data {[email, username, password, firstname, lastname, role ]} -- [Signup details needed]
        """
        try:
            sql = """INSERT INTO users(email, username, password, firstname, lastname, role, status, inserted_at)
                            VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')"""

            """ Encrypt the user password using a hash algorithm before inserting into database """
            hashed_password = generate_password_hash(password)
            status = 0
            inserted_at = datetime.now()

            sql_command = sql.format(email,
                                    username,
                                    hashed_password,
                                    firstname,
                                    lastname,
                                    role,
                                    status,
                                    inserted_at)
            
            self.cur.execute(sql_command)
            return jsonify({'message': 'user registered successfully'}), 200
        except Exception as ex:
                return jsonify({'message': 'Failure to register user. Error is {}'.format(ex)}), 400

    def login_user(self, username, password):
        """Logs in a user

        Arguments:
          data {[username, password ]} -- [Login credentials needed]
        """
        sql = """SELECT username,password FROM users WHERE username='{}'"""
        self.cur.execute(sql.format(username))
        db_user = self.cur.fetchone()
        if not db_user:
            return jsonify({'message': 'No user found'}), 404
        if not check_password_hash(db_user[1], password):
            return jsonify({'message': 'Invalid password'}), 400
        else:
            access_token = create_access_token(identity=username)
            return jsonify({'message': 'successfully logged in',
                            'token': access_token
                            }), 200
    
    def check_duplicate_email(self, the_email):
        '''
            checks the email submitted by user during registration to see if it already exists
        '''

        sql_email = """SELECT email FROM users WHERE email='{}'"""
        self.cur.execute(sql_email.format(the_email))
        db_email = self.cur.fetchone()
        if db_email:
            return True
        else:
            return False
    
    def check_duplicate_username(self, the_username):
        '''
            checks the email submitted by user during registration to see if it already exists
        '''

        sql_username = """SELECT username FROM users WHERE username='{}'"""
        self.cur.execute(sql_username.format(the_username))
        db_username = self.cur.fetchone()
        if db_username:
            return True
        else:
            return False
