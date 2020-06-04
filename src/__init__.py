from flask import Flask, jsonify
from src.users.view import user
from src.courses.view import course
from src.courseModules.view import module
from flask_jwt_extended import JWTManager
from decouple import config
from flask_cors import CORS


app = Flask(__name__)
cors = CORS(app)
app.register_blueprint(user)
app.register_blueprint(course)
app.register_blueprint(module)
app.config['JWT_SECRET_KEY'] = config("SECRET_KEY")
jwt = JWTManager(app)


@app.route('/')
def index():
    return jsonify({"message": "welcome to teachers hub"})
