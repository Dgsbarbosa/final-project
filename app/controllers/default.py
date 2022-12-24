
from flask import render_template, flash, redirect, url_for, request, session
from flask import render_template, flash, redirect, url_for
from flask_login import login_user, logout_user, current_user
from app import app, db, lm
from flask_mail import Mail, Message
from app.models.tables import User, Clients, Orcaments
from app.models.forms import LoginForm
from flask_session import Session
from flask_wtf.csrf import CSRFProtect


@lm.user_loader
def load_user(id):
    
    return User.query.filter_by(id=id).first()

# Rotas
@app.route("/index")
@app.route("/")
def index():
    if not session.get("username"):
        return redirect("/login")
    return render_template(
        "index.html",
        title="Home")

# Increver-se
@app.route("/cadastro_user",  methods=['GET', 'POST'])
def cadastro_user():

    if request.method == 'POST':
        user = User(
            name=request.form['nome'],
            password=request.form['password'],
            username=request.form['username'],
            email=request.form['email']


        )
        db.session.add(user)
        db.session.commit()
        return redirect(url_for("index"))

    return render_template(
        "cadastroUser.html",
        title="Cadastro de Cliente")

# Edit user
@app.route('/edit_user', methods=['GET', 'POST'])
def edit_user():
    if current_user.is_authenticated:
        id_user = current_user

        user = User.query.get(id_user.id)
        print(user.name)
        if request.method == 'POST':

            user.name = request.form['nome']
            user.password = request.form['password']       
            user.username = request.form['username']
            user.email = request.form['email']        
            

            db.session.commit()
            flash("Usuário alterado")
            return redirect(url_for("edit_user"))

    else:
        return redirect(url_for("login"))
    return render_template("perfil.html", user=user,
                           title="Editar Usuário")

# Routes login
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.password == form.password.data:
            login_user(user)
            session["username"] = request.form.get("username")
            
            return redirect(url_for("index"))
        else:
            flash("Invalid login")
            return redirect(url_for("login"))

    return render_template('login.html', form=form)


# Route Profile
@app.route("/perfil")
def perfil():
    return render_template(
        "perfil.html",
        title="Meu Perfil")


# Route Business
@app.route("/negocio")
def negocio():
    return render_template(
        "negocios.html",
        title="Meu Negócio")

# Route Contacts
@app.route("/contatos")
def contatos():
    return render_template(
        "contatos.html",
        title="Contatos")

# Routes Orcamentos
@app.route("/orcamentos", methods=['GET'])
def orcamentos():
    orcaments = Orcaments.query.all()
    return render_template(
        "orcamentos.html",
        title="Orçamentos", orcaments=orcaments)

# View table orcaments
@app.route('/view_orcaments/<int:id>', methods=['GET'])
def view_orcaments(id):
    orcament = Orcaments.query.filter_by(id=id).first_or_404()

    return render_template('viewOrcaments.html', orcament=orcament)


# create orcaments
@app.route("/folha_orcamentos", methods=['GET', 'POST'])
def folha_orcamentos():

    clients = Clients.query.all()

    

    if request.method == 'POST':

        pedido = Orcaments(

            client=request.form['client'],
            pedido=request.form['pedido'],            
            valor=request.form['valor'],
            desconto=request.form['desconto'],
            forma_pagto=request.form['pagto'],
            valor_total=request.form['total']


        )
        print(pedido)

        db.session.add(pedido)
        db.session.commit()
        return redirect(url_for("orcamentos"))

    return render_template(
        "folhaOrcamento.html",
        title="Criar Orçamento", clients=clients)


# View orcament
@app.route('/viewOrcament/<int:id>', methods=['GET'])
def view_orcament(id):
    orcament = Orcaments.query.filter_by(id=id).first_or_404()
    
    return render_template('viewOrcament.html', orcament=orcament)

# Edit Orcament
@app.route('/edit_orcament/<int:id>', methods=['GET', 'POST'])
def edit_orcament(id):
    orcament = Orcaments.query.get(id)
    if request.method == 'POST':

        orcament.client = request.form['client']
        orcament.pedido = request.form['pedido']       
        orcament.valor = request.form['valor']
        orcament.desconto = request.form['desconto']
        orcament.forma_pagto = request.form['pagto']
        orcament.valor_total = request.form['total']

        db.session.commit()
        return redirect(url_for("orcamentos"))

    return render_template("editOrcamento.html", orcament=orcament,
                           title="Editar Orcamento")

# Delete orcaments


@app.route("/delet_orcaments/<int:id>")
def delet_orcaments(id):
    orcament = Orcaments.query.get(id)
    print(orcament)
    db.session.delete(orcament)
    db.session.commit()
    return redirect(url_for("orcamentos"))


# View table clients
@app.route("/clients", methods=['GET'])
def clients():

    clients = Clients.query.all()
    
    return render_template(
        "clients.html",
        title="Clientes", clients=clients)


# Cadastro de Clientes
@app.route("/cadastro_clientes",  methods=['GET', 'POST'])
def cadastro_clientes():

    if request.method == 'POST':
        clients = Clients(
            name=request.form['nome'],
            email=request.form['email'],
            address=request.form['endereco'],
            phone=request.form['telefone'],
            phone2=request.form['telefone2'],

        )
        db.session.add(clients)
        db.session.commit()
        return redirect(url_for("clients"))

    return render_template(
        "cadastroClientes.html",
        title="Cadastro de Cliente")


# Edit client
@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    client = Clients.query.get(id)
    if request.method == 'POST':

        client.name = request.form['nome']
        client.address = request.form['endereco']
        client.phone = request.form['telefone']
        client.phone2 = request.form['telefone2']
        client.email = request.form['email']

        db.session.commit()
        return redirect(url_for("clients"))

    return render_template("editClient.html", client=client,
                           title="Editar Cliente")

# View client
@app.route('/viewClient/<int:id>', methods=['GET'])
def view(id):
    client = Clients.query.filter_by(id=id).first_or_404()

    return render_template('viewClient.html', client=client)


# delete client
@app.route("/delete/<int:id>")
def delete(id):
    clients = Clients.query.get(id)

    db.session.delete(clients)
    db.session.commit()
    return redirect(url_for("clients"))


#contatos
@app.route("/contato", methods=['POST', 'GET'])
def contato():

   
    

    return render_template("contatos.html" )

# Logout
@app.route("/logout")
def logout():
    session["username"] = None
    logout_user()
    return redirect(url_for("index"))
