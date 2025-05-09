from flask import Flask, render_template, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config["SECRET_KEY"] = "your_secret_key_here"


class NameForm(FlaskForm):
    name = StringField("Enter your name:", validators=[DataRequired()])
    submit = SubmitField("Submit")


# Start with an empty list — no default users
data = []


@app.route("/", methods=["GET", "POST"])
def index():
    form = NameForm()
    if form.validate_on_submit():
        name = form.name.data
        message = f"Hello, {name}!"
        data.append({"name": name, "message": message})
        return redirect(url_for("index"))

    return render_template("index.html", form=form, data=data)


if __name__ == "__main__":
    app.run(debug=True)
