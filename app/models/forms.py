from flask_wtf import FlaskForm, CSRFProtect
from wtforms import StringField, PasswordField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Email
csrf = CSRFProtect()

class LoginForm(FlaskForm):
    username = StringField("username", validators=[DataRequired()])
    
    password = PasswordField("password", validators=[DataRequired()])
    
    remember_me = BooleanField("remember_me")

class MyForm(FlaskForm):
    nome = StringField("nome", validators=[DataRequired()])
    email = StringField("email", validators=[DataRequired()])
    endereco = StringField("endereco")
    telefone = StringField("telefone")
    telefone2 = StringField("telefone2")
    



class ContactForm(FlaskForm):    
    name = StringField('Nome', validators=[DataRequired('Nome não pode ficar vazio')])
    email = StringField('E-mail', validators=[DataRequired('E-mail não pode ficar vazio'),Email('Informe um email válido')])
    subject = StringField('Assunto', validators=[DataRequired('Assunto não pode ficar vazio')])
    message = TextAreaField('Mensagem', validators=[DataRequired('Mensagem não pode ficar vazio')])
