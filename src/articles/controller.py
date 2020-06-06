from database_handler import DbConn
from datetime import datetime

now = datetime.now()


class ArticleController:

    """Article controller interfaces with the database."""

    def __init__(self):
        """Initializes the article controller class."""
        conn = DbConn()
        self.cur = conn.create_connection()
        conn.create_organizations_table()
        conn.create_courses_table()
        conn.create_articles_table()

    def query_article(self, article_id):
        ''' selects an article  from database '''
        sql = """ SELECT * FROM articles  WHERE article_id ='{}' """
        sql_command = sql.format(article_id)
        self.cur.execute(sql_command)
        row = self.cur.fetchone()
        return row

    def update_article(self, data, article_id):
        """Updates a article."""
        sql = """UPDATE articles SET article_title='{}', author_name='{}',\
        article_body='{}' ,updated_at='{}' WHERE article_id='{}'"""
        sql_command = sql.format(data['article_title'],
                                 data['author_name'], data['article_body'],
                                 now, article_id)
        self.cur.execute(sql_command)
        sql = """ SELECT * FROM articles  WHERE article_id ='{}' """
        sql_command = sql.format(article_id)
        self.cur.execute(sql_command)
        row = self.cur.fetchone()
        if row:
            return row