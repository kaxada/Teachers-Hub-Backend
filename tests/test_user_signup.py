import unittest
from database_handler import DbConn
from src import app as my_app
import json




class TestUserSignUp(unittest.TestCase):
    '''Tests User Signup Process'''
    def setUp(self):
        '''Initialise Flask application'''
        my_app.testing = True
        self.app = my_app.test_client()


        
    
    def signup_user(self,username, password, email, firstname, lastname, role, confirm_password):
        data = {'username': username, 'password': password, 'email': email, 'firstname': firstname, 'lastname': lastname, 'role': role, 'confirm_password': confirm_password}
        #data = json.dumps(data_dict)
        #print(data)
        
        return self.app.post('/api/v1/auth/signup', json=data)

    def test_user_signup(self):
        '''
        We then call the user signup API method
        '''
        output = self.signup_user('kizza4', 'Test123', 'test4@test.com', 'kizza', 'samuel', 'teacher', 'Test123')
        assert b'user registered successfully' in output.data
