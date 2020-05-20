class Course:

    """Describes the attributes of a course."""
    def __init__(self, **kwargs):
        """Initializes the user model."""
        self.course_name = kwargs.get('course_name')
        self.course_duration = kwargs.get('course_duration')
