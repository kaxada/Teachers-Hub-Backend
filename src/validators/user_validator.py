import re


class ValidateUser:
    """Validate user attributes"""

    def __init__(self, data):
        self.data = data

    def validate_name(self):
        """Validate name and role fields"""
        fields = ['username', 'firstname', 'lastname', 'role',
                  'confirm_password', 'email', 'password']
        if len(self.data.keys()) != 7:
            return "Wrong number of fields, should be 7"
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
        if not len(self.data['password']) > 5:
            return "password should be greater than 5 characters"

    def validate_email(self):
        if 'email' not in self.data.keys():
            return 'email field is missing'
        email_format = re.search(r"([\w\.-]+)@([\w\.-]+)(\.[\w\.]+$)",
                                 self.data['email'])
        if not email_format:
            return "wrong email format"

    def is_valid(self):
        """combines all field validation"""
        if isinstance(self.validate_name(), str):
            return self.validate_name()
        elif isinstance(self.validate_email(), str):
            return self.validate_email()
        elif isinstance(self.validate_password(), str):
            return self.validate_password()
        else:
            return "valid"
