from second_app import db, app
from flask import render_template
from second_app.models import Writer, Book, User

@app.route("/addbook")
def addBook():
    try:
        writer = Writer(name = "maryam")
        book = Book(name = "The Book", writer = writer)
        writer.books.append(book)
        db.session.add(book)
        db.session.commit()
        return "added" + "<a href='books>All books </a>"
    except Exception as ex:
        return str(ex)
    
@app.route("/books")
def showBooks():
    books = Book.query.all()
    return render_template("result.html" , books = books)



@app.route("/")
def home():
    users = User.query.all()
    return render_template("result.html" , users = users)

@app.route("/adduser")
def addUser():
    try:
        user = User(name = "zahra")
        db.session.add(user)
        db.session.commit()
        return "added"
    except Exception as ex:
        return str(ex)
    

if __name__ == "__main__":
    app.run(debug=True)