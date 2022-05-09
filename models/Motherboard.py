from utils.db import db

class Motherboard(db.Model):
    id_motherboard = db.Column(db.Integer, primary_key=True, nullable= False)
    nombre = db.Column(db.String(75), nullable= False)
    fabricante = db.Column(db.String(75), nullable= False)
    zocalo = db.Column(db.String(75), nullable= False)
    chipset = db.Column(db.String(75), nullable= False)
    soporte_memoria = db.Column(db.String(75), nullable= False)
    precio_aproximado= db.Column(db.Integer, nullable= False)
    web = db.Column(db.String(250), nullable= False)

    def __init__(self, nombre, fabricante, zocalo, chipset, soporte_memoria, precio_aproximado, web):
        self.nombre = nombre
        self.fabricante = fabricante
        self.zocalo = zocalo
        self.chipset = chipset
        self.soporte_memoria = soporte_memoria
        self.precio_aproximado = precio_aproximado
        self.web = web