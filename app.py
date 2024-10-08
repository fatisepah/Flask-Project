from flask import Flask, render_template , url_for , request
import os

path = os.path.join("uploads")
os.makedirs(path, exist_ok=True)

app = Flask(__name__)

allowed_extensions = ['png', 'jpg', 'jpeg', 'gif']
def checkfileFormat(fileName):
    return "." in fileName and fileName.rsplit(".",1)[1] in allowed_extensions


@app.route("/")
def index():
    return render_template('form.html')

@app.route("/submit", methods=["POST"])
def showResult():
    email = request.form['email']
    password = request.form['password']
    return render_template('result.html',email = email, password = password)

@app.route("/upload")
def upload():
    return render_template('upload.html')

@app.route("/uploaded" , methods=["POST"])
def savefile():
    theFile = request.files['file']

    if checkfileFormat(theFile.filename):
        try:
            theFile.save(os.path.join(path, theFile.filename))
            return "the file is saved successfully"
        except Exception as e:
            return "there is a error in saving your file !" + "the error is" + e
    else:
        return "the file format is not allowed"