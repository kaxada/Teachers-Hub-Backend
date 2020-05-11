from flask import Flask, Blueprint,render_template, redirect,request,url_for,session,flash,jsonify,json,make_response
from functools import wraps
import uuid
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import (create_access_token,get_jwt_identity, jwt_required)
from src.models.database import *
from src.models.validator import *


db = MyDatabase()
validate = ValidateUser()
login_blueprint = Blueprint('login_blueprint',__name__)



@login_blueprint.route('/auth/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data['username']
    password = data['password']

    if validate.validate_username(username) and validate.validate_password(password):
        return True
    else:
        return False
        
    db.cur.execute("SELECT username,password FROM users WHERE username=%s",[username])
    db_user = db.cur.fetchone()
    if not db_user:
    	return jsonify({'message':'No user found'})

    if not check_password_hash(db_user[1],password):
    	return jsonify({'message':'Invalid password'})

    else:
    	access_token = create_access_token(identity=username)
    	return jsonify({'message':'successfully logged in',
        'token': access_token
    	}), 200

