from utils.db import db

class User(db.Model):
    id_usuario = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(75))
    nombre_cuenta = db.Column(db.String(75))
    password = db.Column(db.String(75))
    admin = db.Column(db.Integer, nullable=True, default="0")

    def __init__(self, email, nombre_cuenta, password, admin):
        self.email = email
        self.nombre_cuenta = nombre_cuenta
        self.password = password
        self.admin = admin