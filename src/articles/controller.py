from database_handler import DbConn


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