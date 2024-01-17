from flask import jsonify, request
from flask_jwt_extended import create_access_token, create_refresh_token
from werkzeug.security import check_password_hash, generate_password_hash
from models import db, NewsPaper, User

# create a function to auth login page
def process_login():
    """check login"""
    password = request.form.get("password")
    email = request.form.get("email")
    
    # 检查邮箱是否存在以及密码是否正确
    user = User.query.filter_by(email=email).first()
    if user and check_password_hash(pwhash=user.password, password=password):
        access_token = create_access_token(identity=email)
        refresh_token = create_refresh_token(identity=email)
        return jsonify(access_token=access_token, refresh_token=refresh_token), 200
    else:
        return jsonify({"msg":"Invalid credentials"}), 401
    

# create a function to register user
def process_register():
    """create a user"""
    hash_and_salted_password = generate_password_hash(
      request.form.get('password'),
      method='pbkdf2:sha256',
      salt_length=8
    )

    # 添加新用户/add new user to db
    new_user = User(
      email=request.form.get('email'),
      name=request.form.get('name'),
      password=hash_and_salted_password,
      username=request.form.get('username')
    )

    db.session.add(new_user)
    db.session.commit()

    return jsonify({"msg":"User created successfully"}), 201


# return user information
def get_user_info():
    """get user info"""
    users = db.session.execute(db.select(User)).scalars() # get all objects
    return jsonify([user.serialize() for user in users]), 200

