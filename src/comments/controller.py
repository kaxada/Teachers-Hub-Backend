from datetime import datetime
from flask import jsonify
from flask_jwt_extended import get_jwt_identity

from database_handler import DbConn
from ..validators.comment_validator import ValidateComment
from src.users.controller import ( conn, cur)

class CommentController:

    """Comment controller interfaces with the database."""

    def __init__(self):
        """Initializes the user controller class."""
        conn.create_courses_table()
        conn.create_comments_table()

    def create_comment(self, data, course_id):
        """Creates a comment."""
        author = get_jwt_identity()['username']
        sql = """INSERT INTO comments(commentBody, commentDateAdded, commentAuthor, courseID)
                        VALUES ('{}', '{}', '{}', '{}')"""
        sql_command = sql.format(data['comment_body'], datetime.now(), author, course_id)
        cur.execute(sql_command)

    def add_new_comment(self, data, course_id):
        validate = ValidateComment(data)
        is_valid = validate.validate_comment_body()
        if is_valid:
            self.create_comment(data, course_id)
            return jsonify({"message": "comment added"}), 201
        else:
            return jsonify({"message": is_valid}), 400

    def fetch_comments(self, course_id):
        ''' selects all available comments from the database '''
        comments = []
        sql = """ SELECT * FROM comments WHERE CourseID='{}'"""
        cur.execute(sql.format(course_id))
        rows = cur.fetchall()
        for row in rows:
            comments.append({
                "comment_id": row[0],
                "comment_body": row[1],
                "comment_date_added": row[2],
                "comment_author": row[3],
                "course_id": row[4]
            })
        return comments
