from flask import jsonify, Blueprint, request
from .controller import ArticleController
from ..validators.article_validator import ValidateArticle

article = Blueprint('article', __name__)
article_controller = ArticleController()


@article.route('/api/v1/articles/<article_id>', methods=['PUT'])
def update_article(article_id):
    """posts a new article"""
    data = request.get_json()

    if data:
        validate_article = ValidateArticle(data)
        if validate_article.validate_article_title() and\
            validate_article.validate_author_name() and\
            validate_article.validate_article_body():
            article_controller.update_article(data, article_id)
            return jsonify({"message": "article updated successfully"}), 200
        elif not validate_article.validate_article_title():
            return jsonify({"message": "enter valid article title"}), 400
        elif not validate_article.validate_author_name():
            return jsonify({"message": "enter valid author name"}), 400
        elif not validate_article.validate_article_body():
            return jsonify({"message": "enter valid article body "}), 400
    else:
        return jsonify({"message": "article details not provided"}), 400


@article.route('/api/v1/articles', methods=['GET'])
def view_all_articles():
    """
    Function enables user to view all the available articles from the database.
    """
    if not article_controller.query_all_articles():
        return jsonify({
            'message': 'No available articles in the database'
        }), 400
    articles = article_controller.query_all_articles()
    return jsonify({
        'articles': articles,
        'message': 'articles fetched!'
    }), 200
