import unittest
from src.users.model import User

class TestUser(unittest.TestCase):
    """ Tests User """

    def setUp(self):
        """Sets up the user class """
        self.user = User(**{'email':'maria@gmail.com','firstname': 'maria', 'role': 'user'})

    def test_user_model(self):
        """
        GIVEN a User model
        WHEN a new User is created
        THEN check the email, hashed_password, username, and role fields are defined correctly
        """
        assert self.user.email == 'maria@gmail.com'
        assert self.user.firstname == 'maria'
        assert self.user.role == 'user'
