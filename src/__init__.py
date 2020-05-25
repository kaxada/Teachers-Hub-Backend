from flask import Flask, jsonify
from src.users.view import user
from src.courses.view import course
from flask_jwt_extended import JWTManager
from decouple import config


app = Flask(__name__)
app.register_blueprint(user)
app.register_blueprint(course)
app.config['JWT_SECRET_KEY'] = config("SECRET_KEY")
jwt = JWTManager(app)


@app.route('/')
def index():
    return jsonify({"message": "welcome to teachers hub"})
