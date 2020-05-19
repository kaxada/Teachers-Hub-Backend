''' file connects to the postgresql database'''
import psycopg2
import uuid


class MyDatabase():
    def __init__(self):
        try:
            self.db = 'sample_db'
            connection = '''dbname={} user=lubwama password=lubwama1'''
            self.conn = psycopg2.connect(connection.format(self.db))
            self.cur = self.conn.cursor()
            self.conn.autocommit = True
            # print(self.db)

            self.cur.execute(
                """
                        CREATE TABLE IF NOT EXISTS courses (
                            course_id SERIAL PRIMARY KEY,
                            courseName TEXT NOT NULL,
                            category_id INTEGER NOT NULL,                        
                            instructor_id INTEGER NOT NULL,
                            duration INTEGER NOT NULL
                            );
                        """
            )
        except Exception as e:
            print(e)
            print("Database connection failed")

    def insert_course(self, courseName, category_id, instructor_id, duration):
        '''
        SQL query to add a course to the database

        '''
        insert_course_query = """
        INSERT INTO courses(courseName, category_id, instructor_id, duration)\
        VALUES('{}', '{}', '{}', '{}');
        """.format(courseName, category_id, instructor_id, duration)
        self.cur.execute(insert_course_query)

    def query(self, table, column, value):
        '''
        Method to query course table rows

        '''

        query = """
        SELECT * FROM {} WHERE {}='{}';
        """.format(table, column, value)
        self.cursor.execute(query)
        row = self.cursor.fetchone()

        return row
