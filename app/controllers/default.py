from flask import render_template
from app import app, db
from app.models.forms import LoginForm
from app.models.tables import User  

status = True
#Rotas
@app.route("/index")
@app.route("/")
def index():
   
    return render_template(
        "index.html",
        title = "Home")

#Routes login
@app.route('/login', methods = ['POST', 'GET'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        print(form.username.data)
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

"""
@app.route("/test", defaults={'name' : None})
@app.route("/test/<name>")
def test(name):
    if name:
        return "Olá, %s!" % name
    else:
        return "Olá usuário"

@app.route("/test2", defaults={'info': None})
@app.route("/test2/<info>")
def test2(info):
    i = User("TESTE", "1234", "Douglas Barbosa", "teste@gmail.com")
    db.session.add(i)
    db.session.commit()
    return "OK"
"""