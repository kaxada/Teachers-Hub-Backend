class Article:

    """Describes the attributes of a Article."""

    def __init__(self, **kwargs):
        """Initializes the article model."""
        self.article_title = kwargs.get('article_title')
        self.author_name = kwargs.get('author_name')
        self.article_body = kwargs.get('article_body')