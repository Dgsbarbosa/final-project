from app import db

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True)
    password = db.Column(db.String)
    name = db.Column(db.String)
    email = db.Column(db.String, unique=True) 

    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)
    

    def __init__(self, username, password, name, email):
        self.username = username
        self.password = password
        self.name = name
        self.email = email

    def __repr__(self):
        return "<User %r>" % self.username


class Clients(db.Model):
    _tablename__ = "clients"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    email = db.Column(db.String, unique=True)
    address = db.Column(db.String)
    bairro = db.Column(db.String)
    cep = db.Column(db.String)
    state = db.Column(db.String)
    phone = db.Column(db.String)
    phone2 = db.Column(db.String)

    def __init__(self, name, email, address, bairro, cep, state, phone, phone2 ):
        self.name = name
        self.email = email
        self.address = address
        self.bairro = bairro
        self.cep = cep
        self.state = state
        self.phone = phone
        self.phone2 = phone2

    def __repr__(self):
        return "<User %r>" % self.name