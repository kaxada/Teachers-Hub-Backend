class Comment:

    """Describes the attributes of comments on a course."""
    def __init__(self, **kwargs):
        """Initializes the user model."""
        self.comment_body = kwargs.get('comment_body')


 