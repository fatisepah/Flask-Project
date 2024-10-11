from datetime import timedelta
from flask import Flask, render_template , request , make_response, session
from flask_sqlalchemy import SQLAlchemy
import os
from flask_migrate import Migrate


app = Flask(__name__)

file_dir = os.path.dirname(__file__)
goal_route = os.path.join(file_dir, "app.db")

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + goal_route

db = SQLAlchemy(app)
migrate = Migrate(app, db)


import second_app.models
import second_app.views

