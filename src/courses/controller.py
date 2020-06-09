from datetime import datetime

from flask_jwt_extended import get_jwt_identity

from database_handler import DbConn


class CourseController:

    """Course controller interfaces with the database."""

    def __init__(self):
        """Initializes the user controller class."""
        conn = DbConn()
        self.cur = conn.create_connection()
        conn.create_courses_table()
        conn.create_enrolled_table()

    def create_course(self, data):
        """Creates a course."""
        sql = """INSERT INTO courses(course_category, course_title, course_description, course_duration, date_added, course_instructor)
                        VALUES ('{}', '{}', '{}', '{}', '{}', '{}')"""
        sql_command = sql.format(data['course_category'], data['course_title'], data['course_description'],
                                 data['course_duration'], datetime.now(), data['course_instructor'])
        self.cur.execute(sql_command)

    def delete_course(self, course_id):
        ''' Deletes a course '''
        sql = """ DELETE FROM courses WHERE courseID ='{}'"""
        sql_command = sql.format(course_id)
        self.cur.execute(sql_command)

    def query_course(self, course_id):
        ''' selects a course from database '''
        sql = """ SELECT * FROM courses  WHERE CourseID ='{}' """
        sql_command = sql.format(course_id)
        self.cur.execute(sql_command)
        row = self.cur.fetchone()
        return row

    def query_course_on_category(self, data):
        """Checks course already exists on category"""
        sql = """SELECT * FROM courses WHERE course_title='{}' AND course_category='{}'"""
        self.cur.execute(sql.format(data["course_title"], data['course_category']))
        row = self.cur.fetchone()
        if row:
            return True
        else:
            return False

    def update_course(self, data, course_id):
        """Updates a course."""
        sql = """UPDATE courses SET course_category='{}', course_duration='{}', course_title='{}', course_description='{}', course_instructor='{}'\
        WHERE CourseID='{}'"""
        sql_command = sql.format(data['course_category'],
                                data['course_duration'], data['course_title'], data['course_description'], data['course_instructor'], course_id)
        self.cur.execute(sql_command)
        sql = """ SELECT * FROM courses  WHERE courseID ='{}' """
        sql_command = sql.format(course_id)
        self.cur.execute(sql_command)
        row = self.cur.fetchone()
        if row:
            return row

    def query_all_courses(self):
        ''' selects all available courses from the database '''
        courses = []
        sql = """ SELECT * FROM courses  """
        self.cur.execute(sql)
        rows = self.cur.fetchall()
        for row in rows:
            courses.append({
                "course_id": row[0],
                "course_category": row[1],
                "course_title": row[2],
                "course_description": row[3],
                "course_duration": row[4],
                "total_enrolled": row[5],
                "date_added": row[6],
                "course_instructor": row[7]
                })
        return courses

    def check_if_already_enrolled(self, course_id):
        """Checks if a user has already enrolled for the course"""
        username = get_jwt_identity()['username']
        sql = """SELECT * FROM enrollement WHERE username= '{}' and CourseID='{}'"""
        self.cur.execute(sql.format(username, course_id))
        row = self.cur.fetchone()
        if row:
            return True
        else:
            return False

    def enroll_course(self, course_id):
        """Enroll for a course"""
        username = get_jwt_identity()['username']
        query = """INSERT INTO enrollement(CourseID, username) VALUES('{}', '{}')"""
        self.cur.execute(query.format(course_id, username))

    def check_instructor_exists(self, course_instructor):
        """Checks instructor exists in courses"""
        sql = """SELECT * FROM users WHERE username='{}' and role='Instructor'"""
        self.cur.execute(sql.format(course_instructor))
        row = self.cur.fetchone()
        if row:
            return True
        else:
            return False