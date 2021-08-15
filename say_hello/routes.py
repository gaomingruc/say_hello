from flask import render_template, url_for, redirect, flash
from say_hello import app, db
from say_hello.forms import PostMessageForm
from say_hello.models import Note


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
