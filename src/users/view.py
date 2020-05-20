from flask import jsonify, Blueprint, request
from .controller import UserController
from src.validators.user_validator import ValidateUser, ValidateUserRegistration


user = Blueprint('user', __name__)
user_controller = UserController()


@user.route('/api/v1/auth/signup', methods=['POST'])
def register_user():
    """Registers a User."""
    data = request.get_json()
    username = data['username']
    password = data['password']
    email = data['email']
    firstname = data['firstname']
    lastname = data['lastname']
    role = data['role']
    confirm_password = data['confirm_password']

    validate = ValidateUserRegistration(
        username, password, confirm_password, email, firstname, lastname, role)
    validation_message, registration_data_is_valid = validate.validate_registration_details()
    if registration_data_is_valid:
        return user_controller.create_user(username, password, email, firstname, lastname, role)
    else:
        return jsonify({"message": "{}".format(validation_message)}), 400



@user.route('/api/v1/auth/login', methods=['POST'])
def login():
    """Logs in a user.
    """
    data = request.get_json()
    username = data['username']
    password = data['password']
    validate = ValidateUser(username, password)

    if validate.validate_username() and \
       validate.validate_password():
        return user_controller.login_user(username, password)
    else:
        return jsonify({
            "message":
            "Enter valid username or password(Lowercase, Uppercase, number)"
        }), 400
