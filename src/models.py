from . import db
from flask_login import UserMixin

class User(UserMixin,db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer,primary_key=True)
    email = db.Column(db.String(100),unique=True)
    password = db.Column(db.String(100))
    nom = db.Column(db.String(100))
    prenom = db.Column(db.String(100))
    phone_number = db.Column(db.String(100))
    address = db.Column(db.String(100))
    
    def __init__(self, email, password, nom, prenom, phone_number, address):
        self.email = email
        self.password = password
        self.phone_number = phone_number
        self.address = address
        self.nom = nom
        self.prenom = prenom

    def __repr__(self):
        return f"<email {self.email} >"

# class Project(db.Model):
#     id = db.Column(db.Integer,primary_key=True)
#     owner = db.Column(db.String(100))
#     description = db.Column(db.String(500))
#     document_path = db.Column(db.String(200)) 
    