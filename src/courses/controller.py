from datetime import datetime

from flask_jwt_extended import get_jwt_identity

from database_handler import DbConn
from src.users.controller import ( conn, cur)

class CourseController:

    """Course controller interfaces with the database."""

    def __init__(self):
        """Initializes the user controller class."""
        conn.create_courses_table()
        conn.create_enrolled_table()

    def create_course(self, data):
        """Creates a course."""
        sql = """INSERT INTO courses(course_category, course_title, course_description, course_duration, date_added, course_instructor)
                        VALUES ('{}', '{}', '{}', '{}', '{}', '{}')"""
        sql_command = sql.format(data['course_category'], data['course_title'], data['course_description'],
                                int(data['course_duration']), datetime.now(), data['course_instructor'])
        cur.execute(sql_command)

    def delete_course(self, course_id):
        ''' Deletes a course '''
        sql = """ DELETE FROM courses WHERE courseID ='{}'"""
        sql_command = sql.format(course_id)
        cur.execute(sql_command)

    def query_course(self, course_id):
        ''' selects a course from database '''
        sql = """ SELECT * FROM courses  WHERE CourseID ='{}' """
        sql_command = sql.format(course_id)
        cur.execute(sql_command)
        return cur.fetchone()

    def query_course_on_category(self, data):
        """Checks course already exists on category"""
        sql = """SELECT * FROM courses WHERE course_title='{}' AND course_category='{}'"""
        cur.execute(sql.format(data["course_title"], data['course_category']))
        return bool(row := cur.fetchone())

    def update_course(self, data, course_id):
        """Updates a course."""
        sql = """UPDATE courses SET course_category='{}', course_duration='{}', course_title='{}', course_description='{}', course_instructor='{}'\
        WHERE CourseID='{}'"""
        sql_command = sql.format(data['course_category'],
                                data['course_duration'], data['course_title'], data['course_description'], data['course_instructor'], course_id)
        cur.execute(sql_command)
        sql = """ SELECT * FROM courses  WHERE courseID ='{}' """
        sql_command = sql.format(course_id)
        cur.execute(sql_command)
        if row := cur.fetchone():
            return row

    def query_all_courses(self):
        ''' selects all available courses from the database '''
        sql = """ SELECT * FROM courses  """
        cur.execute(sql)
        rows = cur.fetchall()
        return [
            {
                "course_id": row[0],
                "course_category": row[1],
                "course_title": row[2],
                "course_description": row[3],
                "course_duration": row[4],
                "total_enrolled": row[5],
                "date_added": row[6],
                "course_instructor": row[7],
            }
            for row in rows
        ]

    def check_if_already_enrolled(self, course_id):
        """Checks if a user has already enrolled for the course"""
        username = get_jwt_identity()['username']
        sql = """SELECT * FROM enrollement WHERE username= '{}' and CourseID='{}'"""
        cur.execute(sql.format(username, course_id))
        return bool(row := cur.fetchone())

    def enroll_course(self, course_id):
        """Enroll for a course"""
        username = get_jwt_identity()['username']
        query = """INSERT INTO enrollement(CourseID, username) VALUES('{}', '{}')"""
        cur.execute(query.format(course_id, username))

    def check_instructor_exists(self, course_instructor):
        """Checks instructor exists in courses"""
        sql = """SELECT * FROM users WHERE username='{}' and role='Instructor'"""
        cur.execute(sql.format(course_instructor))
        return bool(row := cur.fetchone())
    @staticmethod
    def get_enrolled_courses():
        """Checks courses a user has enrolled for."""
        username = get_jwt_identity()['username']
        sql = """SELECT * FROM courses INNER JOIN enrollement ON enrollement.CourseID = courses.CourseID WHERE enrollement.username='{}'"""
        cur.execute(sql.format(username))
        rows = cur.fetchall()
        return [
            {
                "course_id": row[0],
                "course_category": row[1],
                "course_title": row[2],
                "course_description": row[3],
                "course_duration": row[4],
                "total_enrolled": row[5],
                "date_added": row[6],
                "course_instructor": row[7],
            }
            for row in rows
        ]

  