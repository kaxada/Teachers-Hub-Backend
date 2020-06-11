from flask import jsonify, Blueprint, request
from .controller import QuestionsController
from ..validators.questions_validator import ValidateQuestion
from flask_jwt_extended import jwt_required
import psycopg2

from ..users.controller import UserController

question = Blueprint('question', __name__)
question_controller = QuestionsController()
user_controller = UserController()

@question.route('/api/v1/questions/<question_id>', methods=['GET'])
def view_question(question_id):
    """
    Function enables user to view an question from the database.
    """
    try:
        question_id = int(question_id)
        if not question_controller.query_question(question_id):
            return jsonify({
                'message': 'question does not exist in database'
            }), 400
        question = question_controller.query_question(question_id)
        return jsonify({
            'question': {
                '_id': question[0],
                'question_title': question[1],
                'question_author': question[2],
                'created_at': question[3],
                'updates_at': question[4],
                'question_body': question[5],
            },
            'message': 'question fetched!'
        }), 200
    except ValueError:
        return jsonify({
            'message': 'The question id should be an integer!'
        }), 400

@question.route('/api/v1/questions/<question_id>', methods=['PUT'])
@jwt_required
def update_question(question_id):
    """posts a new question"""
    data = request.get_json()

    if data:
        if not question_controller.check_question_author(question_id) and not user_controller.check_admin_user():
            return jsonify({"message": "only Admins and authors allowed"}), 401
        validate_question = ValidateQuestion(data)
        if validate_question.validate_question_title() and\
            validate_question.validate_question_body():
            question_controller.update_question(data, question_id)
            return jsonify({"message": "question updated successfully"}), 200
        elif not validate_question.validate_question_title():
            return jsonify({"message": "enter valid question title"}), 400
        elif not validate_question.validate_question_body():
            return jsonify({"message": "enter valid question body "}), 400
    else:
        return jsonify({"message": "question details not provided"}), 400

@question.route('/api/v1/questions', methods=['POST'])
@jwt_required
def add_new_question():
    """posts a new question"""
    data = request.get_json()

    if data:
        validate_question = ValidateQuestion(data)
        try:
            if validate_question.validate_question_title() and\
                validate_question.validate_question_body():
                question_controller.create_question(data)
                return jsonify({"message": "question added successfully"}), 200
            elif not validate_question.validate_question_title():
                return jsonify({"message": "enter valid question title"}), 400
            elif not validate_question.validate_question_body():
                return jsonify({"message": "enter valid question body "}), 400
        except psycopg2.Error:
            return jsonify({"message": "question title already exists"}), 400
    else:
        return jsonify({"message": "question details not provided"}), 400


@question.route('/api/v1/questions/<question_id>', methods=['DELETE'])
@jwt_required
def delete_question(question_id):
    """
    Function enables admin to delete an question from the database.
    """
    try:
        if not question_controller.check_question_author(question_id) and not user_controller.check_admin_user():
            return jsonify({"message": "only Admins and authors allowed"}), 401
        question_id = int(question_id)
        if not question_controller.query_question(question_id):
            return jsonify({
                'message': 'question does not exist in database'
            }), 400

        question_controller.delete_question(question_id)
        return jsonify({
            'message': 'question deleted successfully!'
        }), 200
    except ValueError:
        return jsonify({
            'message': 'The question id should be an integer!'
        }), 400


@question.route('/api/v1/questions', methods=['GET'])
def view_all_questions():
    """
    Function enables user to view all the available questions from the database.
    """
    if not question_controller.query_all_questions():
        return jsonify({
            'message': 'No available questions in the database'
        }), 400
    questions = question_controller.query_all_questions()
    return jsonify({
        'questions': questions,
        'message': 'questions fetched!'
    }), 200
