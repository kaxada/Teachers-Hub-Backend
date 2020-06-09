class ValidateCourse:
    """validates the courses added to the database

    Returns:
        [boolean] -- [returns true for valid fields and false for invalid
                    fields]
    """

    def __init__(self, data):
        self.data = data

    def validate_course_category(self):
        """validates the course name

        Returns:
            [boolean] -- [True if course name is valid else False]
        """
        try:
            fields = ['course_category', 'course_title', 'course_instructor']
            for field in fields:
                if not isinstance(self.data[field], str)  or \
                self.data[field] == "":
                    return False
                else:
                    return True
        except KeyError:
            return False

    def validate_course_duration(self):
        """validates the course duration

        Returns:
            [True] -- [returns true for valid course duration else false]
        """
        try:
            if self.data['course_duration'] == "" or \
               isinstance(self.data['course_duration'], str):
                return False
            else:
                return True
        except KeyError:
            return False
