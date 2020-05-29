import unittest
from src import app as my_app
from database_handler import DbConn


class TestUserSignUp(unittest.TestCase):
    '''Tests User Signup Process'''

    def setUp(self):
        '''Initialise Flask application'''
        my_app.testing = True
        self.app = my_app.test_client()
        with my_app.app_context():
            conn = DbConn()
            self.cur = conn.create_connection()
            conn.create_users_table()

    def signup_user(self, username, password, email, role, confirm_password):
        data = {'username': username,
                'password': password,
                'email': email,
                'role': role,
                'confirm_password': confirm_password}
        return self.app.post('/api/v1/auth/signup', json=data)

    def test_user_signup(self):
        '''
        We then call the user signup API method
        '''
        output = self.signup_user(
            'kizza5', 'Test123', 'test5@test.com', 'Teacher', 'Test123')
        self.assertIn('user registered successfully',
                      output.data.decode('utf-8'))

    def tearDown(self):
        with my_app.app_context():
            conn = DbConn()
            self.cur = conn.create_connection()
            conn.drop_tables('users')
