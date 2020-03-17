from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import getenv

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = ('DATABASE_URI=mysql+pymysql://root:root@35.246.53.221/gigplanner')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'YOUR_SECRET_KEY'
db = SQLAlchemy(app)

login_manager = LoginManager(app)
login_manager.login_view = 'login'

from application import routes

DATABASE_URI=mysql+pymysql://root:root@35.230.155.181/Flask_blog
