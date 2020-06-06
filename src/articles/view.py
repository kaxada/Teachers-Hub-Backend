from flask import jsonify, Blueprint
from .controller import ArticleController

article = Blueprint('article', __name__)
article_controller = ArticleController()


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