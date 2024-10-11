from datetime import timedelta
from flask import Flask, render_template , request , make_response, session

app = Flask(__name__)

app.secret_key = "secret key"


@app.route("/")
def home():
    if session.get("user_email"):
        return f"welome your email is: {session['user_email']}"
    else:
        return render_template("form.html")

@app.route("/submit", methods=["POST"])
def submitform():
    try:
        email = request.form["email"]
        response = make_response("successful <a href='/'> Home </a>")
        session["user_email"] = email
        session.permanent = True
        app.permanent_session_lifetime = timedelta(days=5)
        return response
    except Exception as ex:
        return f"sorry : {ex}"
