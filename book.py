#! /venv/bin/python
from flask import Flask, redirect, url_for, render_template, flash, request
from flask_sqlalchemy import SQLAlchemy
#from models import *

app = Flask(__name__, instance_relative_config=True)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:kira@localhost/bookstore'

from login.routes import blue
from data.routes import red
#db = SQLAlchemy(app)
app.debug = True

app = Flask(__name__)

db=SQLAlchemy(app)

db.init_app(app)


app.register_blueprint(red)
app.register_blueprint(blue, url_prefix='/data')



if __name__ == "__main__":
    app.run(debug = True)





