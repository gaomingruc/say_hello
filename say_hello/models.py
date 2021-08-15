import datetime
from say_hello import db

# 定义留言数据库


class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String(20), unique=False, nullable=False)
    content = db.Column(db.Text, unique=False, nullable=False)
    create_time = db.Column(db.DateTime, default=datetime.datetime.now)
