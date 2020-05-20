from flask import jsonify, Blueprint, request
from .controller import CourseController
from ..validators.course_validator import ValidateCourse
import psycopg2

course = Blueprint('course', __name__)
course_controller = CourseController()


@course.route('/api/v1/courses', methods=['POST'])
def add_new_course():
    """Registers a Course."""
    data = request.get_json()

    if data:
        validate_course = ValidateCourse(data)
        try:
            if validate_course.validate_course_name() and \
               validate_course.validate_course_duration():
                course_controller.create_course(data)
                return jsonify({"message": "course added successfully"}), 200
            elif not validate_course.validate_course_name():
                return jsonify({"message": "enter valid course name"}), 400
            elif not validate_course.validate_course_duration():
                return jsonify({"message": "enter valid course duration"}), 400
        except psycopg2.Error:
            return jsonify({"message": "course name already exists"}), 400
    else:
        return jsonify({"message": "course details not provided"}), 400

