from app import app



status = True
#Rotas
@app.route("/")
def index():
    if status == False:
        return render_template(
        "home.html",
        title = "Home")
    else:
         return render_template(
        "home2.html",
        title = "Home")

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