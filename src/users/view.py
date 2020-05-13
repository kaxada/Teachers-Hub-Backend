from flask import request, jsonify, Blueprint
from .controller import UserController

user = Blueprint('user', __name__)
user_controller = UserController()

@user.route('/api/v1/auth/signup', methods=['POST'])
def register_user():
    """
    Registers a User
    """
    return jsonify({"message": "user registered successfully"})



