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
        conn.create_courses_table()
        conn.create_modules_table()
        conn.create_modules_content_table()



    def add_new_module(self, course_id, data):
        """Adds a new model to the database."""
        sql = """INSERT into modules(module_title, module_description, module_date_added, CourseID) \
                 VALUES ('{}','{}','{}','{}')"""
        self.cur.execute(sql.format(data['module_title'],
                                    data['module_description'],
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
                "module_date_added": row[3],
                "course_id": row[4]
            })
        return modules

    def add_module_content(self, data, module_id, course_id):
        """adds new module content to database"""
        sql = """INSERT INTO modules_content(module_content, module_content_title, module_content_date_added, ModuleID, CourseID) VALUES \
                ('{}','{}','{}','{}', '{}')"""
        self.cur.execute(sql.format(data['module_content'], data['module_content_title'], datetime.now(), module_id, course_id ))

    def query_existing_module_content(self, module_id, course_id, data):
        """Checks if module content exists"""
        sql = """SELECT * FROM modules_content WHERE ModuleID='{}' and module_content_title='{}' and CourseID='{}'"""
        self.cur.execute(sql.format(module_id, data['module_content_title'], course_id))
        row = self.cur.fetchone()
        if row:
            return True
        else:
            return False

    def check_module_id_exists(self, course_id, module_id):
        """Checks if the module ID exists in the database"""
        sql = """SELECT * from modules WHERE ModuleID='{}' and CourseID='{}'"""
        self.cur.execute(sql.format(module_id, course_id))
        row = self.cur.fetchone()
        if row:
            return True
        else:
            return False

    def register_module_content(self, data, course_id, module_id):
        """register module content"""
        validate = ModuleValidator(data)
        module_valid = validate.is_module_valid()
        if self.check_module_id_exists(course_id, module_id):
            if module_valid == "valid":
                if not self.query_existing_module_content(module_id, course_id, data):
                    self.add_module_content(data, module_id, course_id)
                    return jsonify({"message": "module content added to module {} of course {}".format(module_id, course_id)}), 200
                else:
                    return jsonify({"message": "module content already exists on module {} of course {}".format(module_id, course_id)}), 400
            else:
                return jsonify({"message": module_valid}), 400
        else:
            return jsonify({"message": "module id {} doesnot exist in course {}".format(module_id, course_id)}), 404

    def fetch_module_content(self, course_id, module_id):
        """Fetches module content for a specific id."""
        modules_content = []
        sql = """SELECT * FROM modules_content WHERE ModuleID='{}' and CourseID='{}'"""
        self.cur.execute(sql.format(module_id, course_id))
        rows = self.cur.fetchall()
        for row in rows:
            modules_content.append({
                "module_content_id": row[0],
                "module_content": row[1],
                "module_content_title": row[2],
                "module_content_date_added": row[3],
                "module_id": row[4]
                })
        return modules_content



