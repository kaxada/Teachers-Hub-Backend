import psycopg2
import os
from decouple import config

class DbConn:
    def create_connection(self):
        """ Function that creates the database based on the application
            environment"""
        if os.getenv('APP_SETTINGS') == 'testing':
            self.conn = psycopg2.connect(config("TEST_DATABASE_URL"))
        elif os.getenv('APP_SETTINGS') == 'production':
            self.conn = psycopg2.connect(os.getenv('DATABASE_URL'))
        else:
            self.conn = psycopg2.connect(config("DATABASE_URL"))
        self.conn.autocommit = True
        self.cur = self.conn.cursor()
        return self.cur


    def create_users_table(self):
        """A function to create the users table"""
        self.cur.execute('''CREATE TABLE IF NOT EXISTS users
            (UserID  SERIAL PRIMARY KEY  NOT NULL,
            email VARCHAR(250) NOT NULL UNIQUE,
            username VARCHAR(100) NOT NULL UNIQUE,
            password VARCHAR(100) NOT NULL,
            firstname VARCHAR(100) NOT NULL,
            lastname VARCHAR(100) NOT NULL,
            role VARCHAR(100) NOT NULL); ''')

    def close_DB(self):
        self.conn.commit()
        self.conn.close()