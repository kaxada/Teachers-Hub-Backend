from os import environ

import cloudinary
import cloudinary.api
import cloudinary.uploader
from cloudinary.uploader import upload
from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required

from ..users.controller import UserController
from ..courses.controller import CourseController
from .controller import ModuleController

module = Blueprint('module', __name__)
module_controller = ModuleController()
course_controller = CourseController()
user_controller = UserController()

cloudinary.config(
    cloud_name=environ.get('CLOUDINARY_CLOUD_NAME'),
    api_key=environ.get('CLOUDINARY_API_KEY'),
    api_secret=environ.get('CLOUDINARY_API_SECRET')
)
@module.route('/api/v1/courses/<course_id>/modules', methods=['POST'])
@jwt_required
def add_new_module(course_id):
    """Registers a module to a specific course."""
    if data := request.get_json():
        if not user_controller.check_admin_user():
            return jsonify({"message": "only Admins allowed"}), 401
        return module_controller.add_module_controller(data, course_id)
    else:
        return jsonify({"message": "no data added"}), 400

@module.route('/api/v1/upload', methods=['POST'])
def upload_file():
    if file := request.files['file']:
        result = upload(file, folder="/videos")
        return result["secure_url"]

@module.route('/api/v1/courses/<course_id>/modules', methods=['GET'])
def get_modules(course_id):
    if course_controller.query_course(course_id):
        modules = module_controller.fetch_course_modules(course_id)
        return jsonify({"message": modules }), 200
    else:
        return jsonify({
            'message': 'course doesnot exist in database'
        }), 400

@module.route('/api/v1/courses/<course_id>/modules/<module_id>', methods=['POST'])
@jwt_required
def add_module_content(course_id, module_id):
    if data := request.get_json():
        if not user_controller.check_admin_user():
            return jsonify({"message": "only Admins allowed"}), 401
        return module_controller.register_module_content(data, course_id, module_id)
    else:
        return jsonify({"message": "no data provided"}), 400

@module.route('/api/v1/courses/<course_id>/modules/<module_id>', methods=['GET'])
def fetch_module_content(course_id, module_id):
    """Fetches module content for a specific module"""
    if not module_controller.check_module_id_exists(course_id, module_id):
        return (
            jsonify(
                {
                    'message': f'module {module_id} does not exist on course {course_id}'
                }
            ),
            400,
        )
    module_content = module_controller.fetch_module_content(course_id, module_id)
    return jsonify({
        'module_content': module_content,
    }), 200
