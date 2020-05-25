from database_handler import DbConn


class CourseController:

    """Course controller interfaces with the database."""

    def __init__(self):
        """Initializes the user controller class."""
        conn = DbConn()
        self.cur = conn.create_connection()
        conn.create_organizations_table()
        conn.create_courses_table()

    def create_course(self, data):
        """Creates a course."""
        sql = """INSERT INTO courses(course_name, course_duration)
                        VALUES ('{}', '{}')"""
        sql_command = sql.format(data['course_name'],
                                 data['course_duration'])
        self.cur.execute(sql_command)

    def delete_course(self, course_id):
        ''' Deletes a course '''
        sql = """ DELETE FROM courses WHERE id ='{}'""".format(course_id)        
        self.cur.execute(sql)

    def query_course(self, course_id):
        ''' selects a course from database '''
        sql = """ SELECT * FROM courses  WHERE id ='{}' """.format(course_id)       
        self.cur.execute(sql)
        row = self.cur.fetchone()
        return row
    
