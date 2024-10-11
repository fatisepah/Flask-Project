from flask import Flask, render_template , url_for , request ,redirect


app = Flask(__name__)



@app.route("/")
def index():
    return redirect(url_for("upload"))
    #return redirect("/upload")


@app.route("/upload")
def upload():
    return render_template('upload.html')
