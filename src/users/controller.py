from database_handler import DbConn
from flask import jsonify
from werkzeug.security import check_password_hash, generate_password_hash
from flask_jwt_extended import create_access_token, get_jwt_identity

from datetime import timedelta
from src.validators.user_validator import ValidateUser


conn = DbConn()
cur = conn.create_connection()
class UserController:

    """User controller interfaces with the database."""

    def __init__(self):
        """Initializes the user controller class."""
        conn.create_users_table()
        if not self.check_admin_exists:
            conn.create_default_admin()

    def create_user(self, data):
        """Creates a user.
        Arguments:
          data {[email, username, password, role ]} --
          [Signup details needed]
        """
        sql = """INSERT INTO users(email, username, password, role)
                    VALUES ('{}', '{}', '{}', '{}')"""

        hashed_password = generate_password_hash(data['password'], 'sha256')

        sql_command = sql.format(data['email'],
                                 data['username'],
                                 hashed_password,
                                 data['role'])
        cur.execute(sql_command)

    def register_user_controller(self, data):
        validate = ValidateUser(data)
        is_valid = validate.is_valid()

        if is_valid == "valid":
            if not self.check_duplicate_email(data['email']):
                if not self.check_duplicate_username(data['username']):
                    self.create_user(data)
                    return jsonify({"message":
                                    "user registered successfully"}), 201
                return jsonify({"message": "Username already exists"}), 400
            return jsonify({"message": "Email already exists"}), 400
        return jsonify({"message": is_valid}), 400

    def get_role(self, data):
        sql = """SELECT role FROM users WHERE username = '{}'"""
        cur.execute(sql.format(data['username']))
        if role := cur.fetchone():
            return role

    def login_user(self, data):
        """Logs in a user

        Arguments:
          data {[username, password ]} -- [Login credentials needed]
        """
        validate = ValidateUser(data)
        is_valid = validate.validate_login()
        if is_valid != "valid":
            return jsonify({"message": is_valid}), 400
        role = self.get_role(data)
        identity = {
            'username': data['username'],
            'role': role
        }
        expires = timedelta(hours=23)
        sql = """SELECT username,password FROM users WHERE username='{}'"""
        cur.execute(sql.format(data['username']))
        db_user = cur.fetchone()
        if not db_user:
            return jsonify({'message': 'No user found'}), 404
        if not check_password_hash(db_user[1], data['password']):
            return jsonify({'message': 'Invalid password'}), 400
        access_token = create_access_token(
            identity=identity, expires_delta=expires)
        return jsonify({'message': 'successfully logged in',
                        'token': access_token
                        }), 200

    def check_duplicate_email(self, the_email):
        '''
            checks the email submitted by user
            during registration to see if it already exists
        '''

        sql_email = """SELECT email FROM users WHERE email='{}'"""
        cur.execute(sql_email.format(the_email))
        return bool(db_email := cur.fetchone())

    def check_duplicate_username(self, the_username):
        '''
            checks the email submitted by user
            during registration to see if it already exists
        '''

        sql_username = """SELECT username FROM users WHERE username='{}'"""
        cur.execute(sql_username.format(the_username))
        return bool(db_username := cur.fetchone())

    def get_user_profile_details(self, data):
        sql = """SELECT * FROM users WHERE username = '{}'"""
        cur.execute(sql.format(data['username']))
        if profile_details := cur.fetchone():
            return profile_details

    #pylint: disable=no-self-use
    def check_admin_user(self):
        """Checks the logged in user is an admin"""
        role = get_jwt_identity()['role'][0]
        return role == 'Admin'

    def check_admin_exists(self):
        sql = """SELECT * FROM users WHERE email='{}' and username='{}'"""
        self.cur.execute(sql.format('admin@gmail.com', 'Admin'))
        row = self.cur.fetchone()
        print(row)
        return bool(row)
