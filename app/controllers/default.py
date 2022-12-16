
from flask import render_template, flash, redirect, url_for, request, session

from flask import render_template, flash, redirect, url_for 

from flask_login import login_user, logout_user
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

@app.route("/folha_orcamentos")
def folha_orcamentos():
    return render_template(
        "folhaOrcamento.html",
        title = "Criar Orçamento")

#Route clients
@app.route("/clients", methods=['GET'])
def clients():
    
    clients =  Clients.query.all()
    
    return render_template(
        "clients.html",
        title = "Clientes", clients=clients)


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
        title = "Cadastro de Cliente")

@app.route("/edit/<int:id>", methods=['GET','POST'])
def edit(id):
    client = Clients.query.get(id)
    if request.method == 'POST':
        client.name=request.form['nome']
        client.address=request.form['endereco']
        client.phone=request.form['telefone']
        client.phone2=request.form['telefone2']
        client.email=request.form['email']
        db.session.commit()
        return redirect(url_for("clients"))

    return render_template("editClient.html", client=client,
    title="Editar Cliente") 

@app.route("/delete/<int:id>")
def delete(id):
    clients = Clients.query.get(id)
    db.session.delete(clients)
    db.session.commit()
    return redirect(url_for("clients"))


        

        

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("index"))