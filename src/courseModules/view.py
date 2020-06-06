from flask import Blueprint, jsonify, request
from os import environ
from .controller import ModuleController
from ..courses.controller import CourseController
import cloudinary
import cloudinary.uploader
from cloudinary.uploader import upload
import cloudinary.api
module = Blueprint('module', __name__)
module_controller = ModuleController()
course_controller = CourseController()

cloudinary.config(
    cloud_name=environ.get('CLOUDINARY_CLOUD_NAME'),
    api_key=environ.get('CLOUDINARY_API_KEY'),
    api_secret=environ.get('CLOUDINARY_API_SECRET')
)
@module.route('/api/v1/courses/<course_id>/modules', methods=['POST'])
def add_new_module(course_id):
    """Registers a module to a specific course."""
    data = request.get_json()
    if data:
        return module_controller.add_module_controller(data, course_id)
    else:
        return jsonify({"message": "no data added"}), 400

@module.route('/api/v1/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    if file:
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

@module.route('/api/v1/modules/<module_id>', methods=['POST'])
def add_module_content(module_id):
    data = request.get_json()
    if data:
        return module_controller.register_module_content(data, module_id)
    else:
        return jsonify({"message": "no data provided"}), 400

@module.route('/api/v1/modules/<module_id>', methods=['GET'])
def fetch_module_content(module_id):
    """Fetches module content for a specific module"""
    if not module_controller.check_module_id_exists(module_id):
        return jsonify({
            'message': 'module {} does not exist'.format(module_id)
        }), 400
    modules = module_controller.fetch_module_content(module_id)
    return jsonify({
        'modules': modules,
    }), 200