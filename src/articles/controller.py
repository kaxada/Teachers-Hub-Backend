from database_handler import DbConn
from flask_jwt_extended import get_jwt_identity
from datetime import datetime

class ArticleController:

    """Article controller interfaces with the database."""

    def __init__(self):
        """Initializes the article controller class."""
        conn = DbConn()
        self.cur = conn.create_connection()
        conn.create_articles_table()

    def create_article(self, data):
        """Creates an article."""
        author_name = get_jwt_identity()['username']
        sql = """INSERT INTO articles(article_title, author_name, article_body)
                        VALUES ('{}', '{}','{}')"""
        sql_command = sql.format(data['article_title'],
                                 author_name,
                                 data['article_body'])
        self.cur.execute(sql_command)

    def delete_article(self, article_id):
        ''' Deletes an article '''
        sql = """ DELETE FROM articles WHERE article_id ='{}'"""
        sql_command = sql.format(article_id)
        self.cur.execute(sql_command)

    def query_article(self, article_id):
        ''' selects an article  from database '''
        sql = """ SELECT * FROM articles  WHERE article_id ='{}' """
        sql_command = sql.format(article_id)
        self.cur.execute(sql_command)
        row = self.cur.fetchone()
        return row

    def update_article(self, data, article_id):
        """Updates a article."""
        sql = """UPDATE articles SET article_title='{}',\
        article_body='{}' ,updated_at='{}' WHERE article_id='{}'"""
        sql_command = sql.format(data['article_title'], data['article_body'],
                                 datetime.now(), article_id)
        self.cur.execute(sql_command)
        sql = """ SELECT * FROM articles  WHERE article_id ='{}' """
        sql_command = sql.format(article_id)
        self.cur.execute(sql_command)
        row = self.cur.fetchone()
        if row:
            return row

    def query_all_articles(self):
        ''' selects all available articles from the database '''
        sql = """ SELECT * FROM articles  """
        self.cur.execute(sql)
        rows = self.cur.fetchall()
        return rows

    def check_author(self, article_id):
        """return checks author for authorization purposes"""
        username = get_jwt_identity()['username']
        sql = """SELECT author_name FROM articles WHERE article_id='{}'"""
        self.cur.execute(sql.format(article_id))
        row = self.cur.fetchone()
        if row and row[0] == username:
            return True
        else:
            return False
