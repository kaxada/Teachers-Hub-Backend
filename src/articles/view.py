from flask import jsonify, Blueprint
from .controller import ArticleController

article = Blueprint('article', __name__)
article_controller = ArticleController()


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
        'message': 'articles fetched'
    }), 200