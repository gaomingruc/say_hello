import os
import datetime
from flask import Flask, render_template, url_for, redirect, request, flash
# 表单
from flask_wtf import FlaskForm
from sqlalchemy.sql.operators import desc_op
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length
# 数据库
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config["SECRET_KEY"] = "dev"
db = SQLAlchemy(app)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv(
    'DATABASE_URL', 'sqlite:///' + os.path.join(app.root_path, 'data.db'))
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


# 定义表单类
class PostMessageForm(FlaskForm):
    """
    本表单包含四个组件：姓名、信息、验证切口、提交按钮
    """
    name = StringField(label="姓名", validators=[
                       DataRequired(), Length(min=1, max=20)])
    message = TextAreaField(label="想说的话", validators=[
        DataRequired(), Length(min=1, max=2000)])
    check_info = StringField(label="天王盖地虎", validators=[
        DataRequired(), Length(min=1, max=200)], render_kw={'placeholder': '下一句是？'})
    submit = SubmitField('提交')


# 定义留言数据库
class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String(20), unique=False, nullable=False)
    content = db.Column(db.Text, unique=False, nullable=False)
    create_time = db.Column(db.DateTime, default=datetime.datetime.now)


# 定义路径
@app.route("/", methods=["GET", "POST"])
def index():
    form = PostMessageForm()
    notes = Note.query.order_by(Note.id.desc()).all()
    if form.validate_on_submit() and form.check_info.data == "宝塔镇河妖":
        note = Note(author=form.name.data, content=form.message.data)
        db.session.add(note)
        db.session.commit()
        flash("作者为“%s”，内容为“%s...”的留言已添加" %
              (form.name.data, form.message.data[:10]))
        return redirect(url_for("index"))
    return render_template("base.html", form=form, notes=notes)
