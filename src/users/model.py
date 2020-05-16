class User:

    """Describes the attributes of a user."""
    def __init__(self, **kwargs):
        """Initializes the user model."""
        self.email = kwargs.get('email')
        self.firstname = kwargs.get('firstname')
        self.lastname = kwargs.get('lastname')
        self.username = kwargs.get('username')
        self.password = kwargs.get('password')
        self.confirm_password = kwargs.get('confirm_password')
        self.role = kwargs.get('role')
