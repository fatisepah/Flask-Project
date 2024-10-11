
from flask import Flask, render_template , abort

app = Flask(__name__)


@app.route("/")
def index():
    abort(404) 


@app.errorhandler(404)
def showError(error):
    return render_template("error_404.html") , 404