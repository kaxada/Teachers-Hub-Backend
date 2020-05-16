from database_handler import DbConn
from flask import jsonify
from werkzeug.security import check_password_hash
from flask_jwt_extended import create_access_token


class UserController:

    """User controller interfaces with the database."""

    def __init__(self):
        """Initializes the user controller class."""
        conn = DbConn()
        self.cur = conn.create_connection()
        conn.create_users_table()

    def create_user(self, data):
        """Creates a user."""
        sql = """INSERT INTO users(email, username, password, role)
                        VALUES ('{}', '{}', '{}', '{}')"""
        sql_command = sql.format(data['email'],
                                 data['username'],
                                 data['role'])
        self.cur.execute(sql_command)

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
