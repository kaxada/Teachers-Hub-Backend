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

    def create_article(self, data):
        """Creates an article."""
        sql = """INSERT INTO articles(article_title,author_name,article_body)
                        VALUES ('{}', '{}','{}')"""
        sql_command = sql.format(data['article_title'],
                                 data['author_name'],
                                 data['article_body'])
        self.cur.execute(sql_command)