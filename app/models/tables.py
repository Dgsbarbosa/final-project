from app import db
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
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
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(150))
    email = db.Column(db.String, unique=True)
    address = db.Column(db.String)
    phone = db.Column(db.String)
    phone2 = db.Column(db.String)
    pedidos = db.relationship('Orcaments', backref='clients', lazy=True)

    def __init__(self, name, email, address, phone, phone2):
        self.name = name
        self.email = email
        self.address = address
        self.phone = phone
        self.phone2 = phone2
        

    def __repr__(self):
        return "<Clients %r>" % self.name



class Orcaments(db.Model):
    _tablename__ = "orcaments"
    id = db.Column(db.Integer, primary_key=True)
    pedido_id = db.Column(db.Integer, autoincrement=True)
    client_id = db.Column(db.Integer, db.ForeignKey('clients.id'), nullable=False)
    
    
    def __init__(self, pedido_id, client_id):
        self.pedido_id = pedido_id
        self.client_id = client_id
        
    def __repr__(self):
        return "<Orcaments %r>" % self.client_id


