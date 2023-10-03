import os

import psycopg2
from decouple import config
from werkzeug.security import generate_password_hash


class DbConn:

    def create_connection(self):
        """Function that creates the database based on the application
        environment."""
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
        """A function to create the users table."""
        self.cur.execute('''CREATE TABLE IF NOT EXISTS users
            (UserID  SERIAL PRIMARY KEY  NOT NULL,
            email VARCHAR(250) NOT NULL UNIQUE,
            username VARCHAR(100) NOT NULL UNIQUE,
            password VARCHAR(100) NOT NULL,
            role VARCHAR(100) NOT NULL); ''')

    def create_default_admin(self):
        """Creates a default administrator """
        hashed_password = generate_password_hash('Administrator1', 'sha256')
        sql = """INSERT INTO users(email, username, password, role) VALUES
              ('{}', '{}', '{}', '{}')"""
        self.cur.execute(sql.format('admin@gmail.com', 'Admin', hashed_password, 'Admin'))

    def create_enrolled_table(self):
        """A function to create the course table."""
        self.cur.execute('''CREATE TABLE IF NOT EXISTS enrollement
        (EnrollID  SERIAL PRIMARY KEY  NOT NULL,
         CourseID INTEGER REFERENCES courses(CourseID) ON DELETE CASCADE,
         username VARCHAR(100) REFERENCES users(username) ON DELETE CASCADE); ''')

    def create_modules_table(self):
        """Creates modules table."""
        self.cur.execute('''CREATE TABLE IF NOT EXISTS modules(
            ModuleID SERIAL PRIMARY KEY NOT NULL,
            module_title VARCHAR(250) NOT NULL,
            module_description VARCHAR(255) NOT NULL,
            module_date_added DATE NOT NULL,
            CourseID INTEGER REFERENCES courses(CourseID) ON DELETE CASCADE);''')

    def create_modules_content_table(self):
        """Creates modules content table."""
        self.cur.execute('''CREATE TABLE IF NOT EXISTS modules_content(
            ModuleContentID SERIAL PRIMARY KEY NOT NULL,
            module_content VARCHAR(500) NOT NULL,
            module_content_title VARCHAR(255) NOT NULL,
            module_content_date_added DATE NOT NULL,
            ModuleID INTEGER REFERENCES modules(ModuleID) ON DELETE CASCADE,
            CourseID INTEGER REFERENCES courses(CourseID) ON DELETE CASCADE);''')

    def create_organizations_table(self):
        """A function to create the organization table."""
        self.cur.execute('''CREATE TABLE IF NOT EXISTS organizations
        (OrganizationID  SERIAL PRIMARY KEY  NOT NULL,
        organization_name VARCHAR(250) NOT NULL UNIQUE
        ); ''')

    def create_courses_table(self):
        """A function to create the course table."""
        self.cur.execute('''CREATE TABLE IF NOT EXISTS courses
        (CourseID  SERIAL PRIMARY KEY  NOT NULL,
        course_category VARCHAR(250) NOT NULL,
        course_title VARCHAR(255) NOT NULL,
        course_description VARCHAR(500) NOT NULL,
        course_duration INTEGER NOT NULL,
        total_enrolled INTEGER,
        date_added DATE NOT NULL,
        course_instructor VARCHAR(255) REFERENCES users(username) ON DELETE CASCADE); ''')

    def create_comments_table(self):
        """Creates the comments table for each course"""
        self.cur.execute('''CREATE TABLE IF NOT EXISTS comments(
            commentID SERIAL PRIMARY KEY NOT NULL,
            commentBody VARCHAR(255) NOT NULL,
            commentDateAdded TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
            commentAuthor VARCHAR(255) REFERENCES users(username) \
            ON DELETE CASCADE,
            CourseID INTEGER REFERENCES courses(CourseID) ON DELETE CASCADE); ''')

    def create_articles_table(self):
        """A function to create the articles table."""
        self.cur.execute('''CREATE TABLE IF NOT EXISTS articles
        (article_id  SERIAL PRIMARY KEY  NOT NULL,
        article_title VARCHAR(300) NOT NULL,
        author_name VARCHAR(255) REFERENCES users(username) ON DELETE CASCADE,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
        article_body TEXT NOT NULL ); ''')

    def create_questions_table(self):
        """A function to create the questions table."""
        self.cur.execute('''CREATE TABLE IF NOT EXISTS questions
        (question_id  SERIAL PRIMARY KEY  NOT NULL,
        question_title VARCHAR(300) NOT NULL,
        question_author VARCHAR(255) REFERENCES users(username) ON DELETE CASCADE,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
        question_body TEXT NOT NULL ); ''')

    def drop_tables(self, table_name):
        """ Drops the tables that exist in the database"""
        sql = """ DROP TABLE {} CASCADE; """
        self.cur.execute(sql.format(table_name))
        print(f"Table '{table_name}' successfully dropped")

    def close_DB(self):
        self.conn.commit()
        self.conn.close()
