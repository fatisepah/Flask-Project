
from flask import Flask, render_template , request , make_response

app = Flask(__name__)


@app.route("/")
def home():
    if request.cookies.get("user_email"):
        return f"welome your email is: {request.cookies['user_email']}"
    else:
        return render_template("form.html")

@app.route("/submit", methods=["POST"])
def submitform():
    try:
        email = request.form["email"]
        response = make_response("successful <a href='/'> Home </a>")
        response.set_cookie("user_email", email)
        return response
    except Exception as ex:
        return f"sorry : {ex}"

