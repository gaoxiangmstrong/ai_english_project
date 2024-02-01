from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from datetime import datetime
from sqlalchemy import Integer, String, Text, TIMESTAMP, CheckConstraint
from flask_migrate import Migrate


app = Flask(__name__)

class Base(DeclarativeBase):
  pass

db = SQLAlchemy(model_class=Base)
migrate = Migrate(app, db)

# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///news-reading.db"
# initialize the app with the extension
db.init_app(app)

# create the table User with id name email password 
class User(db.Model):
  __tablename__ = "users"
  id: Mapped[int] = mapped_column(Integer,primary_key=True)
  name: Mapped[str] = mapped_column(String(50))
  email: Mapped[str] = mapped_column(String(255))
  # 账号和密码/ username and password
  username: Mapped[str] = mapped_column(String, unique=True, nullable=False)
  password: Mapped[str] = mapped_column(String, nullable=False)
  reads = relationship('Read', back_populates="user")

  def serialize(self):
     return {
        "id": self.id,
        "name": self.name,
        "email": self.email,
        "username": self.username,
        "password": self.password
     }

# create the table New with id title content category created_at updated_at difficulty
class NewsPaper(db.Model):
    __tablename__= "newsPapers"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(255))
    content: Mapped[str] = mapped_column(Text)
    category: Mapped[str] = mapped_column(String(255))
    created_at: Mapped[datetime] = mapped_column(TIMESTAMP, default=datetime.now)
    updated_at: Mapped[datetime] = mapped_column(TIMESTAMP, default=datetime.now, onupdate=datetime.now)
    difficulty: Mapped[int] = mapped_column(Integer, CheckConstraint('difficulty BETWEEN 1 AND 10'))
    reads = relationship('Read', back_populates='newsPaper')
    
    # 输出一个字典数据/ return a dictionay data
    def serialize(self):
        return {
            "id": self.id,
            "title": self.title,
            "content": self.content,
            "category": self.category,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
            "difficulty": self.difficulty
        }
    
class Read(db.Model):
    __tablename__ = "reads"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    newsPaper_id = db.Column(db.Integer, db.ForeignKey('newsPapers.id'))
    created_at = db.Column(db.TIMESTAMP, default=datetime.now)
    user = relationship('User', back_populates='reads')
    newsPaper = relationship('NewsPaper', back_populates='reads')

# 创建数据库/create the database tables
with app.app_context():
   db.create_all()



# # 创建一个用户/create a dummy user
# with app.app_context():
#    user = User(name="John", email="john@example.com", username="John", password="password")
#    db.session.add(user)
#    db.session.commit()

# # 创建一个新闻/create a dummy news
# with app.app_context():
#    newspaper = NewsPaper(title="News Title", content="There are so many things happended nowadays...", category="News Category", difficulty=5, created_at=datetime.now())
#    db.session.add(newspaper)
#    db.session.commit()

# # 关联read的关系/ relates user to newspaper
# with app.app_context():
#    read = Read(user_id=1, newsPaper_id=1, created_at=datetime.now())
#    db.session.add(read)
#    db.session.commit()

   
# if __name__ == '__main__':
#     app.run()

   

   
