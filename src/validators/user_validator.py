import re


class ValidateUser:
    """Validate user attributes"""

    def __init__(self, data):
        self.data = data

    def validate_login_credentials(self):
        """Validates login username"""
        login_fields = ["username", "password"]
        try:
            if len(self.data.keys()) != 2:
                return "Enter only username and password"
            for field in login_fields:
                if not self.data[field]:
                    return field + " cannot be blank"
                if field not in self.data.keys():
                    return field + " is missing"
                if not isinstance(self.data[field], str):
                    return "Enter string value at {}".format(field)
        except KeyError:
            return "Invalid key added"

    def validate_name(self):
        """Validate name and role fields"""
        fields = ['username', 'role', 'confirm_password', 'email', 'password']
        if len(self.data.keys()) != 5:
            return "Wrong number of fields, should be 5"
        try:
            for field in fields:
                if field not in self.data.keys():
                    return '{} field is missing'.format(field)
                if self.data[field] == "":
                    return field + " cannot be blank"
                if not isinstance(self.data[field], str):
                    return "Enter string value at {}".format(field)
        except KeyError:
            return "Invalid Key added"

    def validate_password(self):
        ''' Method validates a user's password '''

        lower_case = re.search(r"[a-z]", self.data['password'])
        upper_case = re.search(r"[A-Z]", self.data['password'])
        numbers = re.search(r"[0-9]", self.data['password'])

        if self.data['password'] != self.data['confirm_password']:
            return "passwords dont match"

        if not all((lower_case, upper_case, numbers)):
            return "password should be lower, upper and values"
        if not len(self.data['password']) >= 5:
            return "password should be greater than or equal to 5 characters"

    def validate_email(self):
        if 'email' not in self.data.keys():
            return 'email field is missing'
        email_format = re.search(r"([\w\.-]+)@([\w\.-]+)(\.[\w\.]+$)",
                                 self.data['email'])
        if not email_format:
            return "wrong email format"

    def validate_login(self):
        """validates login fields"""
        if isinstance(self.validate_login_credentials(), str):
            return self.validate_login_credentials()
        else:
            return "valid"

    def validate_user_role(self):
        if self.data['role'] != 'Admin' and \
            self.data['role'] != 'Teacher' and \
            self.data['role'] != 'Institution':
            return "Role must be either Admin, Teacher, Institution"

    def is_valid(self):
        """combines all field validation"""
        if isinstance(self.validate_name(), str):
            return self.validate_name()
        elif isinstance(self.validate_email(), str):
            return self.validate_email()
        elif isinstance(self.validate_password(), str):
            return self.validate_password()
        elif isinstance(self.validate_user_role(), str):
            return self.validate_user_role()
        else:
            return "valid"
