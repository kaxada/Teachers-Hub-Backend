class ValidateQuestion:
    """validates the questions added to the database

    Returns:
        [boolean] -- [returns true for valid fields and false for invalid
                    fields]
    """

    def __init__(self, data):
        self.data = data

    def validate_question_title(self):
        """validates the question title

        Returns:
            [boolean] -- [True if article title is valid else False]
        """
        try:
            return (
                isinstance(self.data['question_title'], str)
                and self.data['question_title'] != ""
            )
        except KeyError:
            return False

    def validate_question_body(self):

        """validates the question_body

        Returns:
            [boolean] -- [True if article_body is valid else False]
        """
        try:
            return (
                isinstance(self.data['question_body'], str)
                and self.data['question_body'] != ""
            )
        except KeyError:
            return False