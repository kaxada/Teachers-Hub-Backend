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
            if not isinstance(self.data['question_title'], str)  or \
            self.data['question_title'] == "":
                return False
            else:
                return True
        except KeyError:
            return False

    def validate_question_body(self):

        """validates the question_body

        Returns:
            [boolean] -- [True if article_body is valid else False]
        """
        try:
            if not isinstance(self.data['question_body'], str)  or \
            self.data['question_body'] == "":
                return False
            else:
                return True
        except KeyError:
            return False