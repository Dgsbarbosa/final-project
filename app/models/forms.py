from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SelectField, TextAreaField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    username = StringField("username", validators=[DataRequired()])
    
    password = PasswordField("password", validators=[DataRequired()])
    
    remember_me = BooleanField("remember_me")

class MyForm(FlaskForm):
    nome = StringField("nome", validators=[DataRequired()])
    email = StringField("email")
    endereco = StringField("endereco")
    telefone = StringField("telefone")
    telefone2 = StringField("telefone2")
    submt = SubmitField('enviar')