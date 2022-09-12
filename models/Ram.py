from utils.db import db

class Ram(db.Model):
    id_ram = db.Column(db.Integer, primary_key=True , nullable = False)
    nombre = db.Column(db.String(75), nullable = False)
    fabricante = db.Column(db.String(75), nullable = False)
    capacidad = db.Column(db.String(75), nullable = False)
    velocidad = db.Column(db.String(75), nullable = False)
    formato = db.Column(db.String(75), nullable = False)
    tipo = db.Column(db.String(75), nullable = False)
    precio_aproximado = db.Column(db.Integer, nullable = False)
    web = db.Column(db.String(250), nullable = False)

    def __init__(self, nombre, fabricante, capacidad, velocidad, formato, tipo, precio_aproximado, web):
        self.nombre = nombre
        self.fabricante = fabricante
        self.capacidad = capacidad
        self.velocidad = velocidad
        self.formato = formato
        self.tipo = tipo
        self.precio_aproximado = precio_aproximado
        self.web = web