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
            fields = ['course_category', 'course_title', 'course_instructor','course_duration']
            for field in fields:
                return isinstance(self.data[field], str) and self.data[field] != ""
        except KeyError:
            return False

    def validate_course_duration(self):
        """validates the course duration

        Returns:
            [True] -- [returns true for valid course duration else false]
        """
        try:
            return bool(int(self.data['course_duration']))
        except (KeyError, ValueError):
            return False
