from flask import Flask

# initialize the flask application
app = Flask(__name__)

# setup a test route
@app.route('/')
def hello():
    return 'hello world!'