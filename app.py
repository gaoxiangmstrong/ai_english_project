# from werkzeug.security import generate_password_hash, check_password_hash
from flask import Flask, jsonify, render_template, request
from models import db, NewsPaper, User
from flask_jwt_extended import create_access_token, create_refresh_token, get_jwt_identity, jwt_required, JWTManager
from auth import process_login, process_register, get_users_info
from datetime import timedelta
from flask_cors import CORS
from data_access import get_user_newspapers


# 连接数据库/connect to db
app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///news-reading.db'
db.init_app(app)

# 令牌config
jwt = JWTManager(app)
app.config['SECRET_KEY'] = 'super-secret'
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(hours=10) # acess_token终止时间
app.config["JWT_REFRESH_TOKEN_EXPIRES"] = timedelta(days=30) # refresh_token终止时间



@app.route('/')
def hello():
  return jsonify("Hello World")


@app.route('/register', methods=["GET", "POST"])
def register():
    # 加密以及salt it/encoidng and salt
    if request.method == "POST":
        return process_register()
    return render_template("register.html")


@app.route("/refresh", methods=["POST"])
@jwt_required(refresh=True)
def refresh():
    identity = get_jwt_identity()
    access_token = create_access_token(identity=identity)
    return jsonify(access_token=access_token)


@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
       return process_login()
    return render_template("login.html")


@app.route('/logout')
def logout():
   pass


# 从/user/<id>/newspapers中获取所有的 newspapers
@app.route('/user/<int:user_id>/newspapers')
def user_newspapers(user_id):
    newspapers = get_user_newspapers(user_id)
    dic_newspaper = [np.serialize() for np in newspapers]
    return jsonify(dic_newspaper)


@app.route('/users', methods=["GET"])
@jwt_required()
def user():
   return get_users_info()



if __name__=="__main__":
  app.run(debug=True)
