from flask import jsonify, Blueprint, request
from .controller import ArticleController
from ..validators.article_validator import ValidateArticle
import psycopg2

article = Blueprint('article', __name__)
article_controller = ArticleController()


@article.route('/api/v1/articles', methods=['POST'])
def add_new_article():
    """posts a new article"""
    data = request.get_json()

    if data:
        validate_article = ValidateArticle(data)
        try:
            if validate_article.validate_article_title() and\
                validate_article.validate_author_name() and\
                validate_article.validate_article_body():
                article_controller.create_article(data)
                return jsonify({"message": "article added successfully"}), 200
            elif not validate_article.validate_article_title():
                return jsonify({"message": "enter valid article title"}), 400
            elif not validate_article.validate_author_name():
                return jsonify({"message": "enter valid author name"}), 400
            elif not validate_article.validate_article_body():
                return jsonify({"message": "enter valid article body "}), 400
        except psycopg2.Error:
            return jsonify({"message": "article title already exists"}), 400
    else:
        return jsonify({"message": "article details not provided"}), 400


@article.route('/api/v1/articles/<article_id>', methods=['DELETE'])
def delete_article(article_id):
    """
    Function enables admin to delete an article from the database.
    """
    try:
        article_id = int(article_id)
        if not article_controller.query_article(article_id):
            return jsonify({
                'message': 'article does not exist in database'
            }), 400

        article_controller.delete_article(article_id)
        return jsonify({
            'message': 'article deleted successfully!'
        }), 200
    except ValueError:
        return jsonify({
            'message': 'The article id should be an integer!'
        }), 400


@article.route('/api/v1/articles/<article_id>', methods=['GET'])
def view_article(article_id):
    """
    Function enables user to view an article from the database.
    """
    try:
        article_id = int(article_id)
        if not article_controller.query_article(article_id):
            return jsonify({
                'message': 'article does not exist in database'
            }), 400
        article = article_controller.query_article(article_id)
        return jsonify({
            'article': {
                '_id': article[0],
                'article_title': article[1],
                'author_name': article[2],
                'created_at': article[3],
                'updates_at': article[4],
                'article_body': article[5],
            },
            'message': 'article fetched!'
        }), 200
    except ValueError:
        return jsonify({
            'message': 'The article id should be an integer!'
        }), 400
