from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField,SubmitField, BooleanField, TextAreaField,validators
from wtforms.validators import DataRequired, Email
import email_validator

class LoginForm(FlaskForm):
    username = StringField("username", validators=[DataRequired()])
    
    password = PasswordField("password", validators=[DataRequired()])
    
    remember_me = BooleanField("remember_me")

class MyForm(FlaskForm):
    name = StringField("nome", validators=[DataRequired()])
    email = StringField("email", validators=[DataRequired()])
    endereco = StringField("endereco")
    telefone = StringField("telefone")
    telefone2 = StringField("telefone2")
    



class ContactForm(FlaskForm):    
    name = StringField(label='Name', validators=[DataRequired('Nome não pode ficar vazio')])
    email = StringField(label='Email', validators=[DataRequired('E-mail não pode ficar vazio'),Email('Informe um email válido')])
    subject = StringField('Assunto', validators=[DataRequired('Assunto não pode ficar vazio')])
    message = TextAreaField('Mensagem', validators=[DataRequired('Mensagem não pode ficar vazio')])
    submit = SubmitField("Enviar")