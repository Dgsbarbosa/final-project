from app import db
from sqlalchemy import Column, Integer, DateTime
from sqlalchemy.orm import relationship
import datetime



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
    client = db.Column(db.String)
    date = db.Column(DateTime, default=datetime.datetime.utcnow)
    pedido = db.Column(db.String)
    valor = db.Column(db.Integer)
    desconto = db.Column(db.Integer)

    forma_pagto = db.Column(db.String)
    valor_total = db.Column(db.Integer)

    
    
    def __init__(self, client, date, pedido, valor, desconto, forma_pagto, valor_total):
        self.client =client
        self.date = date
        self.pedido = pedido
        self.valor = valor
        self.desconto = desconto
        self.forma_pagto = forma_pagto
        self.valor_total = valor_total
        
        
    def __repr__(self):
        return "<Orcaments %r>" % self.client


