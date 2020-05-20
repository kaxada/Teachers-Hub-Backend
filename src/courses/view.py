from flask import jsonify, Blueprint, request
from .controller import CourseController

course = Blueprint('course', __name__)
course_controller = CourseController()


@course.route('/api/v1/courses', methods=['POST'])
def add_new_course():
    """Registers a Course."""
    data = request.get_json()
    if data:
        course_controller.create_course(data)
        return jsonify({"message": "course registered successfully"}), 200
    else:
        return jsonify({"message": "course details not provided"}), 400
