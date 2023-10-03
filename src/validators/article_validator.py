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
            return (
                isinstance(self.data['article_title'], str)
                and self.data['article_title'] != ""
            )
        except KeyError:
            return False

    def validate_article_body(self):

        """validates the article_body

        Returns:
            [boolean] -- [True if article_body is valid else False]
        """
        try:
            return (
                isinstance(self.data['article_body'], str)
                and self.data['article_body'] != ""
            )
        except KeyError:
            return False