from flask import jsonify, Blueprint, request
from .controller import UserController
from src.validators.user_validator import ValidateUser
from flask_jwt_extended import jwt_required, get_jwt_identity

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
    validate = ValidateUser(data)

    if data:
        return user_controller.login_user(data)
    else:
        return jsonify({
            "message": validate.validate_login()
        }), 400


@user.route('/api/v1/auth/profile', methods=['GET'])
@jwt_required
def get_user_profile():
    current_user = get_jwt_identity()
    profile_details = user_controller.get_user_profile_details(current_user)
    return jsonify(username=profile_details[2], email=profile_details[1], role=profile_details[4]), 200
