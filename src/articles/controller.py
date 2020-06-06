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

    def query_all_articles(self):
        ''' selects all available articles from the database '''
        sql = """ SELECT * FROM articles  """
        self.cur.execute(sql)
        rows = self.cur.fetchall()
        return rows