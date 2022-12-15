from flask import Flask, Response, request, redirect, session, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate
from flask_login import LoginManager


app = Flask(__name__)

app.config.from_object('config')
db = SQLAlchemy(app)
migrate = Migrate(app, db, render_as_batch=True)

manager = Manager(app)

lm = LoginManager()
lm.init_app(app)



from app.models import tables, forms 
from app.controllers import default







