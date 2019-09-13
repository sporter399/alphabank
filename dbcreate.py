from flask import Flask, request, redirect, render_template, session
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Boolean

import os
import sqlite3


app = Flask(__name__)

app.config['DEBUG'] = True
project_dir = os.path.dirname(os.path.abspath(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///{}".format(os.path.join(project_dir, "alphabank.db"))
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)

db.create_all()