from flask import Flask, jsonify
from src.users.view import user

app = Flask(__name__)
app.register_blueprint(user)


@app.route('/')
def index():
    return jsonify({"message": "welcome to teachers hub"})
