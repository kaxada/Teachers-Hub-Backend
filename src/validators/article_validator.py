class ValidateArticle:
    """validates the articles added to the database

    Returns:
        [boolean] -- [returns true for valid fields and false for invalid
                    fields]
    """

    def __init__(self, data):
        self.data = data

    def validate_article_title(self):
        """validates the article title

        Returns:
            [boolean] -- [True if article title is valid else False]
        """
        try:
            if not isinstance(self.data['article_title'], str)  or \
            self.data['article_title'] == "":
                return False
            else:
                return True
        except KeyError:
            return False

    def validate_article_body(self):

        """validates the article_body

        Returns:
            [boolean] -- [True if article_body is valid else False]
        """
        try:
            if not isinstance(self.data['article_body'], str)  or \
            self.data['article_body'] == "":
                return False
            else:
                return True
        except KeyError:
            return False