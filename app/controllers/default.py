from flask import render_template, flash
from app import app, db
from app.models.forms import LoginForm
from app.models.tables import User  
from flask_login import login_user


#Rotas
@app.route("/index")
@app.route("/")
def index():
   
    return render_template(
        "index.html",
        title = "Home")

#Routes login
@app.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.password == form.data.password:
            login_user(user)
            flash("Logged in.")
        else:
            flash("Invalid login")    
    else:
        print(form.errors)
    return render_template('login.html', form=form)

#Route clients
@app.route("/clients")

def clients():
    return render_template(
        "clients.html",
        title = "Clientes"
    )
    
@app.route("/perfil")
def perfil():
    return render_template(
        "perfil.html",
        title = "Meu Perfil")

@app.route("/negocio")
def negocio():
    return render_template(
        "negocios.html",
        title = "Meu Negócio")

@app.route("/contatos")
def contatos():
    return render_template(
        "contatos.html",
        title = "Contatos")

@app.route("/orcamentos")
def orcamentos():
    return render_template(
        "orcamentos.html",
        title = "Orçamentos")

@app.route("/folha-de-orcamento")
def folha_orcamentos():
    return render_template(
        "folhaOrcamento.html",
        title = "Criar Orçamento")

@app.route("/cadastro-clientes")
def cadastro_clientes():
    return render_template(
        "cadastroClientes.html",
        title = "Orçamentos")
