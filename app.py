from flask import Flask, render_template, url_for, redirect, request, flash
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length


app = Flask(__name__)
app.config["SECRET_KEY"] = "dev"


class PostMessageForm(FlaskForm):
    """
    本表单包含四个组件：姓名、信息、验证切口、提交按钮
    """
    name = StringField(label="姓名", validators=[
                       DataRequired(), Length(min=1, max=20)])
    message = TextAreaField(label="想说的话", validators=[
        DataRequired(), Length(min=1, max=200)])
    check_info = StringField(label="天王盖地虎", validators=[
        DataRequired(), Length(min=1, max=200)], render_kw={'placeholder': '下一句是？'})
    submit = SubmitField('提交')


@app.route("/", methods=["GET", "POST"])
def index():
    form = PostMessageForm()
    if form.validate_on_submit():
        flash(form.name.data)
        flash(form.message.data)
        return redirect(url_for("index"))
    return render_template("base.html", form=form)
