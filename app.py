from flask import Flask, jsonify, render_template, request
from werkzeug.security import generate_password_hash, check_password_hash
from models import db, NewsPaper, User
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required, JWTManager


# 连接数据库/connect to db
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///news-reading.db'
db.init_app(app)



@app.route('/')
def hello():
  return jsonify("Hello World")


@app.route('/register', methods=["GET", "POST"])
def register():
    # 加密以及salt it/encoidng and salt
    if request.method == "POST":
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

        # 返回添加成功json/return success message in json
        return jsonify({"msg":"User created successfully"}), 201
    return render_template("register.html")



@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        
        # check if email can be found and the password is correct
        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(pwhash=user.password, password=password):
            access_token = create_access_token(identity=username)
            return jsonify(access_token=access_token), 200
        else:
            return jsonify({"msg":"Invalid credentials"}), 401
        
    return render_template("login.html")


@app.route('/logout')
def logout():
   pass


@app.route('/user')
def user():
   pass




# 查看是否能从news-reading.db中读取数据/check if can read data from news-reading.db
@app.route("/newspaper")
def newsPapar():
  # render newspaper from news-reading.db
  data = NewsPaper.query.all()
  # jsonify serialize data
  datas = jsonify([newsPaper.serialize() for newsPaper in data])
  print(datas)
  return render_template("newspaper.html", datas=datas)
  







if __name__=="__main__":
  app.run(debug=True)
