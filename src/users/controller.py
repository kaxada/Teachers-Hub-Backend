from database_handler import DbConn
from flask import request, jsonify
from decouple import config

class UserController:
    """
    This user controller interfaces with the database
    """

    def __init__(self):
        conn = DbConn()
        self.cur = conn.create_connection()
        conn.create_users_table()

    def create_user(self, data):
        """
        Creates a user
        """
        sql = """INSERT INTO users(email, username, password, role)
                        VALUES ('{}', '{}', '{}', '{}')"""
        sql_command = sql.format(data['email'],
                                 data['username'],
                                 hashed_password,
                                 data['role'])
        self.cur.execute(sql_command)