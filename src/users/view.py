from flask import jsonify, Blueprint, request
from .controller import UserController
from src.validators.user_validator import ValidateUser

user = Blueprint('user', __name__)
user_controller = UserController()


@user.route('/api/v1/auth/signup', methods=['POST'])
def register_user():
    """Registers a User."""
    data = request.get_json()
    if data:
        return user_controller.register_user_controller(data)
    else:
        return jsonify({"message": "no data added"}), 400


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
