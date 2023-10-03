class ValidateComment:
    """validates the comments added to a course

    Returns:
        [boolean] -- [returns true for valid fields and false for invalid
                    fields]
    """

    def __init__(self, data):
        self.data = data

    def validate_comment_body(self):
        """validates the comment body

        Returns:
            [boolean] -- [True if course name is valid else False]
        """
        return (
            isinstance(self.data['comment_body'], str)
            and self.data['comment_body'] != ""
        )

