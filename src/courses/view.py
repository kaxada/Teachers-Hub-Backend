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


@course.route('/api/v1/courses/<course_id>', methods=['DELETE'])
def delete_course(course_id):
    """
    Function enables admin to delete a course from the database.
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD

=======
    
>>>>>>> An administrator should be able to delete a course
=======
>>>>>>> removing trailing white space
=======
>>>>>>> removing trailing white space
    """
    try:
        course_id = int(course_id)
        if not course_controller.query_course(course_id):
            return jsonify({
                'message': 'Course does not exist in database'
            }), 400

        course_controller.delete_course(course_id)
        return jsonify({
            'message': 'Course deleted!'
        }), 200
    except ValueError:
        return jsonify({
            'message': 'The course id should be an integer!'
        }), 400
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======

>>>>>>> An administrator should be able to delete a course
=======
>>>>>>> remove trailing white space
=======
=======
>>>>>>> An administrator should be able to view a single course


@course.route('/api/v1/courses/<course_id>', methods=['GET'])
def view_course(course_id):
    """
<<<<<<< HEAD
    Function enables user to view a course from the database.
=======
    Function enables admin to view a course from the database.
    
>>>>>>> An administrator should be able to view a single course
    """
    try:
        course_id = int(course_id)
        if not course_controller.query_course(course_id):
            return jsonify({
                'message': 'Course does not exist in database'
            }), 400
        course = course_controller.query_course(course_id)
        return jsonify({
            'course': {
                '_id': course[0],
                'course_name': course[1],
                'course_duration': course[2]
            },
            'message': 'course fetched!'
        }), 200
    except ValueError:
        return jsonify({
            'message': 'The course id should be an integer!'
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
        }), 400
>>>>>>> An administrator should be able to view a single course
=======
        }), 400
>>>>>>> removing trailing white space
=======
        }), 400


@course.route('/api/v1/courses/<course_id>', methods=['PUT'])
def update_course(course_id):
    """
    Function enables user to modify a course from the database.
    """
    data = request.get_json()

    if data:
        validate_course = ValidateCourse(data)
        try:
            if validate_course.validate_course_name() and \
               validate_course.validate_course_duration():
                course_controller.update_course(data, course_id)
                return jsonify({"message": "course updated successfully"}), 200
            elif not validate_course.validate_course_name():
                return jsonify({"message": "enter valid course name"}), 400
            elif not validate_course.validate_course_duration():
                return jsonify({"message": "enter valid course duration"}), 400
        except ValueError:
            return jsonify({"message": "course id should be an integer"}), 400
    else:
        return jsonify({"message": "course details not provided"}), 400
>>>>>>> An admin should be able to update a course
=======
        }), 400
>>>>>>> An administrator should be able to view a single course
=======
        }), 400
>>>>>>> removing trailing white space
