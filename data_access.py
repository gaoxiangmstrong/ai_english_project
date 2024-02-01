# data_access.py
from models import User, NewsPaper, Read, app, db, datetime

def get_user_newspapers(user_id):
    return NewsPaper.query.join(Read).join(User).filter(User.id == user_id).all()


# 写一些测试用的代码
# 创建新闻以及关联
# # 创建一个用户/create a dummy user
def new_user(name, email, username, password):
  with app.app_context():
    user = User(name=name, email=email, username=username, password=password)
    db.session.add(user)
    db.session.commit()

# 创建一个新闻/create a dummy news
def new_newspaper(title, content, category, difficulty):
  with app.app_context():
    newspaper = NewsPaper(title=title, content=content, category=category, difficulty=difficulty, created_at=datetime.now())
    db.session.add(newspaper)
    db.session.commit()

# # 关联read的关系/ relates user to newspaper
def add_relations(newsPaper_id):
  with app.app_context():
    read = Read(user_id=1, newsPaper_id=newsPaper_id, created_at=datetime.now())
    db.session.add(read)
    db.session.commit()

# 创建一个给user添加一个newspaper
def main():
  # 添加一个newspaper
  new_newspaper("spiderman", "this is the advanture of spiderman ...", category="advanture", difficulty=5)
  # 添加一个关系
  add_relations(2)




