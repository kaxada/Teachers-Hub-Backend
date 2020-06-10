class Question:

    """Describes the attributes of a Question."""

    def __init__(self, **kwargs):
        """Initializes the question model."""
        self.question_title = kwargs.get('question_title')
        self.question_author = kwargs.get('question_author')
        self.question_body = kwargs.get('question_body')