from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required

from .controller import CommentController
from ..courses.controller import CourseController

comment = Blueprint('comment', __name__)
comment_controller = CommentController()
course_controller = CourseController()

@comment.route('/api/v1/courses/<course_id>/comments', methods=['POST'])
@jwt_required
def add_new_comment(course_id):
    """adds comment to course."""
    if data := request.get_json():
        if not course_controller.query_course(course_id):
            return jsonify({
                    'message': 'Course does not exist in database'
                }), 404
        comment_controller.add_new_comment(data, course_id)
        return jsonify({"message": "comment added successfully"}), 200
    else:
        return jsonify({"message": "No data"}), 400



@comment.route('/api/v1/courses/<course_id>/comments', methods=['GET'])
def fetch_comment(course_id):
    """gets comment to course."""
    if not course_controller.query_course(course_id):
        return jsonify({
                'message': 'Course does not exist in database'
            }), 400
    comments = comment_controller.fetch_comments(course_id)
    return jsonify({"comments": comments}), 200
