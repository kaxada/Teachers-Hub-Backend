from datetime import datetime
from flask import jsonify
from database_handler import DbConn

from ..courses.controller import CourseController
from ..validators.module_validator import ModuleValidator

course_controller = CourseController()


class ModuleController:
    def __init__(self):
        """Initializes the user controller class."""
        conn = DbConn()
        self.cur = conn.create_connection()
        conn.create_organizations_table()
        conn.create_courses_table()
        conn.create_modules_table()



    def add_new_module(self, course_id, data):
        """Adds a new model to the database."""
        sql = """INSERT into modules(module_title, module_description, module_content, module_date_added, CourseID) \
                 VALUES ('{}','{}','{}','{}', '{}')"""
        self.cur.execute(sql.format(data['module_title'],
                                    data['module_description'],
                                    data['module_content'],
                                    datetime.now(),
                                    course_id))
    def check_duplicate_module(self, data, course_id):
        """checks if the module already exists on the course"""
        sql = """SELECT * from modules WHERE module_title='{}' and CourseID='{}'"""
        self.cur.execute(sql.format(data['module_title'], course_id))
        row = self.cur.fetchone()
        if row:
            return True
        else:
            return False


    def add_module_controller(self, data, course_id):
        validate = ModuleValidator(data)
        is_valid = validate.is_valid()

        if is_valid == "valid":
            if course_controller.query_course(course_id):
                if not self.check_duplicate_module(data, course_id):
                    self.add_new_module(course_id, data)
                    return jsonify({"message":
                                    "module successfully added"}), 201
                else:
                    return jsonify({"message": "module already exists on course"}), 400
            return jsonify({
                    'message': 'course doesnot exist in database'
                }), 400
        return jsonify({"message": is_valid}), 400

    def fetch_course_modules(self, course_id):
        """Fetches all modules on a course"""
        modules = []
        sql = """SELECT * FROM modules WHERE CourseID='{}'"""
        self.cur.execute(sql.format(course_id))
        rows = self.cur.fetchall()
        for row in rows:
            modules.append({
                "module_id": row[0],
                "module_title": row[1],
                "module_description": row[2],
                "module_content": row[3],
                "module_date_added": row[4],
                "course_id": row[5]
            })
        return modules

