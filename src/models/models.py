from src.models.database.database import MyDatabase

db = MyDatabase()


class Course:
    ''' 
    Class validates the courses added to the database 

    '''

    def __init__(self, courseName, categoryId, instructorId, duration):

        self.courseName = courseName
        self.categoryId = categoryId
        self.instructorId = instructorId
        self.duration = duration

    def insert_course(self):
        '''
        Method enables admin to add a course to the database
        :returns:
        False - if that course is already in the database.
        A dictionary object of the course that has been added.

        '''
        if db.query('courses', 'courseName', self.courseName) is not None:
            return False

        db.insert_course(self.courseName, self.categoryId, self.instructorId,
                         self.duration)
        course = db.query('courses', 'name', self.courseName)
        return {
            'course_id': course[0],
            'courseName': course[1],
            'category_id': course[2],
            'instructor_id': course[3],
            'duration': course[4],

        }
