class Course:

    """Describes the attributes of a course."""
    def __init__(self, **kwargs):
        """Initializes the user model."""
        self.course_category = kwargs.get('course_category')
        self.course_title = kwargs.get('course_title')
        self.course_description = kwargs.get('course_description')
        self.course_duration = kwargs.get('course_duration')

 