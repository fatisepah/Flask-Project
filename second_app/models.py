from second_app import db, app

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)

class Writer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    writer_id = db.Column(db.Integer , db.ForeignKey("writer.id"))
    writer = db.relationship("Writer", backref = db.backref("books"))

# ایجاد کانتکست اپلیکیشن برای db.create_all()
with app.app_context():
    db.create_all()