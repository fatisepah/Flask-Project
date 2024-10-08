from flask import Flask , render_template , url_for, request


app = Flask(__name__)


@app.route("/")
def index():
    data = request.args['id']
    return data