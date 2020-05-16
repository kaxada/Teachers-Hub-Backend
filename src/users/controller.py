from database_handler import DbConn


class UserController:

    """User controller interfaces with the database."""

    def __init__(self):
        """Initializes the user controller class."""
        conn = DbConn()
        self.cur = conn.create_connection()
        conn.create_users_table()

    def create_user(self, data):
        """Creates a user."""
        sql = """INSERT INTO users(email, username, password, role)
                        VALUES ('{}', '{}', '{}', '{}')"""
        sql_command = sql.format(data['email'],
                                 data['username'],
                                 data['role'])
        self.cur.execute(sql_command)
