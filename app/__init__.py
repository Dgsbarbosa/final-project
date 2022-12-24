from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_session import Session
from flask_mail import Mail, Message
from app.models.forms import ContactForm


app = Flask(__name__)

mail= Mail(app)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'dg.developer.1988@gmail.com'
app.config['MAIL_PASSWORD'] = 'Dod@1988'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

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







