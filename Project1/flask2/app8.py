from datetime import timedelta
from flask import Flask, render_template , request , make_response, session
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

file_dir = os.path.dirname(__file__)
goal_route = os.path.join(file_dir, "app.db")

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + goal_route

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False)
    #email = db.Column(db.String(120), nullable=False)

# ایجاد کانتکست اپلیکیشن برای db.create_all()
with app.app_context():
    db.create_all()

@app.route("/")
def home():
    users = User.query.filter(User.username.like("%fati%")).all()
    return render_template("result.html" , users = users)
@app.route("/add")
def addUser():
    #user = User(username = request.args["username"], email = request.args["email"])
    try:
        user = User(username = "fati")
        db.session.add(user)
        db.session.commit()
        return "added"
    except Exception as ex:
        return str(ex)

@app.route("/update")
def updateUser():
    #user = User(username = request.args["username"], email = request.args["email"])
    try:
        goal_user = User.query.filter_by(username = "fati").first()
        goal_user.username = "fatemeh"
        db.session.commit()
        return "updated" + "<a href='/'> Home </a>" 
    except Exception as ex:
        return str(ex)


@app.route("/delete")
def deleteUser():
    #user = User(username = request.args["username"], email = request.args["email"])
    try:
        goal_user = User.query.filter_by(username = "fati").first()
        db.session.delete(goal_user)
        db.session.commit()
        return "deleted" + "<a href='/'> Home </a>" 
    except Exception as ex:
        return str(ex)


if __name__ == "__main__":
    app.run(debug=True)
