from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_session import Session

app = Flask(__name__)

app.config.from_object('config')
app.config["SESSION_PERMANENT"]=False
app.config["SESSION_TYPE"]="filesystem"
Session(app)
lm = LoginManager()

lm.init_app(app)

db = SQLAlchemy(app)
migrate = Migrate(app, db, render_as_batch=True)

manager = Manager(app)





from app.models import tables, forms 
from app.controllers import default







