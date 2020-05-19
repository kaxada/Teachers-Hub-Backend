import re


class ValidateUser:
    ''' Class to validate user attributes '''

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def validate_username(self):
        '''
        Method validates a user's username
        '''

        if not self.username or self.username.isspace() or not isinstance(
                self.username, str):
            return False
        else:
            return True

    def validate_password(self):
        ''' Method validates a user's password '''

        lower_case = re.search(r"[a-z]", self.password)
        upper_case = re.search(r"[A-Z]", self.password)
        numbers = re.search(r"[0-9]", self.password)

        if not self.password or not all((lower_case, upper_case, numbers))\
                or not len(self.password) > 5:
            return False
        else:
            return True


class ValidateCourse:
    ''' 
    Class validates the courses added to the database 

    '''

    def __init__(self, categoryId, instructorId, duration, courseName):
        self.categoryId = categoryId
        self.instructorId = instructorId
        self.duration = duration
        self.courseName = courseName

    def validate_categoryId(self):
        ''' 
        function validates the category id

        '''
        if not self.categoryId and not isinstance(
                self.categoryId, int):
            return False
        else:
            return True

    def validate_coursename(self):
        ''' function validates the course name '''

        if not self.courseName or self.courseName.isspace() or not isinstance(
                self.courseName, str):
            return False
        else:
            return True

    def validate_instructorId(self):
        ''' 
        function validates the instructor id
        '''
        if not self.instructorId and not isinstance(
                self.instructorId, int):
            return False
        else:
            return True

    def validate_Duration(self):
        ''' 
        function validates the course Duration

        '''
        if not self.duration and not isinstance(
                self.duration, int):
            return False
        else:
            return True
