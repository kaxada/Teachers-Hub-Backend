from flask_jwt_extended import get_jwt_identity
from datetime import datetime
from src.users.controller import ( conn, cur)

class QuestionsController:

    """Question controller interfaces with the database."""

    def __init__(self):
        """Initializes the questions controller class."""
        conn.create_questions_table()

    def create_question(self, data):
        """Creates a question."""
        question_author = get_jwt_identity()['username']
        sql = """INSERT INTO questions(question_title, question_author, question_body)
                        VALUES ('{}', '{}','{}')"""
        sql_command = sql.format(data['question_title'],
                                 question_author,
                                 data['question_body'])
        cur.execute(sql_command)

    def delete_question(self, question_id):
        ''' Deletes a question '''
        sql = """ DELETE FROM questions WHERE question_id ='{}'"""
        sql_command = sql.format(question_id)
        cur.execute(sql_command)

    def query_question(self, question_id):
        ''' selects a question  from database '''
        sql = """ SELECT * FROM questions  WHERE question_id ='{}' """
        sql_command = sql.format(question_id)
        cur.execute(sql_command)
        row = cur.fetchone()
        return row

    def update_question(self, data, question_id):
        """Updates a question."""
        sql = """UPDATE questions SET question_title='{}',\
        question_body='{}' ,updated_at='{}' WHERE question_id='{}'"""
        sql_command = sql.format(data['question_title'], data['question_body'],
                                 datetime.now(), question_id)
        cur.execute(sql_command)
        sql = """ SELECT * FROM questions  WHERE question_id ='{}' """
        sql_command = sql.format(question_id)
        cur.execute(sql_command)
        row = cur.fetchone()
        if row:
            return row

    def query_all_questions(self):
        ''' selects all available questions from the database '''
        sql = """ SELECT * FROM questions  """
        cur.execute(sql)
        rows = cur.fetchall()
        return rows

    def check_question_author(self, question_id):
        """return checks author for authorization purposes"""
        username = get_jwt_identity()['username']
        sql = """SELECT question_author FROM questions WHERE question_id='{}'"""
        cur.execute(sql.format(question_id))
        row = cur.fetchone()
        if row and row[0] == username:
            return True
        else:
            return False
