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

    def validate_author_name(self):

        """validates the author_name

        Returns:
            [boolean] -- [True if author_name is valid else False]
        """
        try:
            if not isinstance(self.data['author_name'], str)  or \
            self.data['author_name'] == "":
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