# 表单
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length


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
