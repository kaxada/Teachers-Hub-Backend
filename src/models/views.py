from flask import Blueprint, request, jsonify
from src.models.database.database import MyDatabase
from src.models.validator import ValidateCourse
from src.models.models import Course


db = MyDatabase()
blueprint = Blueprint('blueprint', __name__)


@blueprint.route('/courses', methods=['POST'])
# @jwt_required  # check if user is an admin
def add_course():
    """
    Function adds a course to the courses table.
    :returns:
    A success message and the course.
    """

    try:
        data = request.get_json()

        courseName = data.get('coursename')
        category_id = data.get('category_id')
        instructor_id = data.get('instructor_id')
        duration = data.get('duration')

        validate_course = ValidateCourse(
            courseName, category_id, instructor_id, duration)

        course = Course(courseName, category_id, instructor_id, duration)
        if validate_course.validate_coursename is False:
            return jsonify({
                'message': 'Course Name is invalid'
            }), 400
        elif validate_course.validate_categoryId is False:
            return jsonify({
                'message': 'Category cannot be empty'
            }), 400
        elif validate_course.validate_instructorId is False:
            return jsonify({
                'message': 'The instructor field is invalid'
            }), 400
        elif validate_course.validate_Duration is False:
            return jsonify({
                'message': 'The duration field is invalid'
            }), 400

        course_dict = course.insert_course()
        if not course_dict:
            return jsonify({
                'message': 'This course already exists!'
            }), 400
        return jsonify({
            'product': course_dict,
            'message': 'Course added successfully!'
        }), 201
    except ValueError:
        return jsonify({
            'message': 'The duration must be a number!'
        }), 400
