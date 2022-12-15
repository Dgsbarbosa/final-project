from flask import render_template, flash, redirect, url_for, request, session
from flask_login import login_user, logout_user, session_protected
from app import app, db, lm

from app.models.tables import User, Clients
from app.models.forms import LoginForm, MyForm
 


@lm.user_loader
def load_user(id):
    return User.query.filter_by(id=id).first()


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
        if user and user.password == form.password.data:            
            login_user(user)            
            return redirect(url_for("index"))
        else:
            flash("Invalid login")    
            return redirect(url_for("login"))
  
    return render_template('login.html', form=form)


#Route clients
@app.route("/clients", methods=['GET'])
def clients():
    
    clients =  Clients.query.filter_by().all()
    print(clients)
    print("--------")
    return render_template(
        "clients.html",
        title = "Clientes", clients=clients)

#Route Profile        
@app.route("/perfil")
def perfil():
    return render_template(
        "perfil.html",
        title = "Meu Perfil")

# Route Business
@app.route("/negocio")
def negocio():
    return render_template(
        "negocios.html",
        title = "Meu Negócio")

# Route Contacts
@app.route("/contatos")
def contatos():
    return render_template(
        "contatos.html",
        title = "Contatos")

# Routes Orcamentos
@app.route("/orcamentos")
def orcamentos():
    return render_template(
        "orcamentos.html",
        title = "Orçamentos")

# Route cadastra orcamento
@app.route("/folha_orcamentos")
def folha_orcamentos():
    return render_template(
        "folhaOrcamento.html",
        title = "Criar Orçamento")

# Cadastro de Clientes
@app.route("/cadastro_clientes",  methods=['GET', 'POST'])
def cadastro_clientes():
    form = MyForm()
    if form.validate_on_submit():
        session['nome'] = form.nome.data
        session['email'] = form.email.data
        session['telefone'] = form.telefone.data
        session['telefone2'] = form.telefone2.data

        return redirect(url_for('cadastrado'))

    print(form.nome)
    print(form.email)
    print(form.endereco)
    print(form.telefone)
    return render_template(
        "cadastroClientes.html",
        form=form)
        
@app.route('/cadastrado')
def cadastrado():
    return render_template('clients.html')
        

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("index"))