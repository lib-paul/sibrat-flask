from utils.db import db

class Motherboard(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable= False)
    nombre = db.Column(db.String(75), nullable= False)
    fabricante = db.Column(db.String(75), nullable= False)
    zocalo = db.Column(db.String(75), nullable= False)
    chipset = db.Column(db.String(75), nullable= False)
    soporte_memoria = db.Column(db.String(75), nullable= False)
    factor_forma = db.Column(db.String(75), nullable=False)
    precio_aproximado= db.Column(db.Integer, nullable= False)
    web = db.Column(db.String(250), nullable= False)

    def __init__(self, nombre, fabricante, zocalo, chipset, soporte_memoria, factor_forma, precio_aproximado, web):
        self.nombre = nombre
        self.fabricante = fabricante
        self.zocalo = zocalo
        self.chipset = chipset
        self.soporte_memoria = soporte_memoria
        self.factor_forma = factor_forma
        self.precio_aproximado = precio_aproximado
        self.web = web

    def caracteristicas_motherboard():
        caracteristicas={
            "1" : "ID",
            "2" : "Nombre",
            "3" : "Fabricante",
            "4" : "Zocalo",
            "5" : "Soporte Memoria",
            "6" : "Precio Aproximado",
            "7" : "Opciones"
        }
        return caracteristicas

    def columnas_motherboard():
        columnas = [
            "id",
            "nombre",
            "fabricante",
            "zocalo",
            "soporte_memoria",
            "precio_aproximado",
        ]
        return columnas
