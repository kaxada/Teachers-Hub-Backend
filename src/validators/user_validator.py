import re
from validate_email import validate_email
from src.users.controller import UserController


class ValidateUser:
    ''' Class to validate user attributes '''

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def validate_username(self):
        '''
        Method validates a user's username
        '''

        if not self.username or self.username.isspace() or not isinstance(
                self.username, str):
            return False
        else:
            return True

    def validate_password(self):
        ''' Method validates a user's password '''

        lower_case = re.search(r"[a-z]", self.password)
        upper_case = re.search(r"[A-Z]", self.password)
        numbers = re.search(r"[0-9]", self.password)

        if not self.password or not all((lower_case, upper_case, numbers))\
                or not len(self.password) > 5:
            return False
        else:
            return True


class ValidateUserRegistration:
    ''' Class to validate user attributes '''

    def __init__(self, username, password, confirm_password, email, firstname, lastname, role):
        self.username = username
        self.password = password
        self.email = email
        self.firstname = firstname
        self.lastname = lastname
        self.confirm_password = confirm_password
        self.role = role

    def validate_registration_details(self):
        '''
        The regular expressions below search the user password to confirm to see if it contains  upper case, lower case letters and a number
        '''
        lower_case = re.search(r"[a-z]", self.password)
        upper_case = re.search(r"[A-Z]", self.password)
        numbers = re.search(r"[0-9]", self.password)

        user_controller = UserController()

        db_username = user_controller.check_duplicate_username(self.username)

        db_email = user_controller.check_duplicate_email(self.email)

        if not self.username:
            return 'username field is blank', False
        elif self.username.isspace():
            return 'username field contains a space', False
        elif not isinstance(self.username, str):
            return 'username field must be a String', False
        elif db_username:
            return 'username is already in use!', False
        elif not self.password:
            return 'password field is blank', False
        elif not all((lower_case, upper_case, numbers)):
            return 'password must contain at least 1 upper case, 1 lower case letter and 1 number', False
        elif not len(self.password) > 5:
            return 'password must be longer than 5 characters', False
        elif self.confirm_password != self.password:
            return 'The confirm password value is different from the password', False
        elif not self.firstname:
            return 'firstname field is blank', False
        elif self.firstname.isspace():
            return 'firstname must not contain a space', False
        elif not isinstance(self.firstname, str):
            return 'firstname must be a string', False
        elif not self.lastname:
            return 'lastname field is blank', False
        elif self.lastname.isspace():
            return 'lastname must not contain a space', False
        elif not isinstance(self.lastname, str):
            return 'lastname must be a string', False
        elif not self.role:
            return 'role field is blank', False
        elif self.role.isspace():
            return 'role field contains a space', False
        elif not isinstance(self.role, str):
            return 'role field must be a String', False
        elif not self.email:
            return 'email field is blank', False
        elif not validate_email(self.email):
            return 'You have entered an invalid Email', False
        elif db_email:
            return 'email is already in use!', False
        else:
            return 'All user registration details are okay', True
