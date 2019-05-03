from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SECRET_KEY'] = '250d2a22815f08b89db09f804cef4f09'
db = SQLAlchemy(app)

from flaskblog import  routes