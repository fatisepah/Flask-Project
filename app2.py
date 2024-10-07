from flask import Flask , render_template , url_for, request


app = Flask(__name__)


@app.route("/")
def index():
    myList = [1,2,3,4,5]
    return render_template("index.html", myList = myList)

#@app.route("/welcome")
#def welcome():
#    return render_template("index.html" , name = "Mohammad")

@app.route("/welcome/<name>")
def welcome(name):
    url_for("static", filename="style.css")
    return render_template("index.html" , name = name)