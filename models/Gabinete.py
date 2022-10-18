from utils.db import db

class Gabinete(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable= False)
    nombre = db.Column(db.String(75), nullable= False)
    fabricante = db.Column(db.String(75), nullable= False)
    tipo_estructura = db.Column(db.String(75), nullable= False)
    soporte_motherboard = db.Column(db.String(75), nullable= False)
    precio_aproximado = db.Column(db.Integer, nullable= False)
    web = db.Column(db.String(250), nullable= False)

    def __init__(self, nombre, fabricante, tipo_estructura, soporte_motherboard, precio_aproximado, web):
        self.nombre = nombre
        self.fabricante = fabricante
        self.tipo_estructura = tipo_estructura
        self.soporte_motherboard = soporte_motherboard
        self.precio_aproximado = precio_aproximado
        self.web = web


    def caracteristicas_gabinete():
        caracteristicas={
            "1" : "ID",
            "2" : "Nombre",
            "3" : "Fabricante",
            "4" : "Estructura",
            "5" : "Soporte MB",
            "6" : "Precio",
            "7" : "Opciones"
        }
        return caracteristicas

    def columnas_gabinete():
        columnas = [
            "id",
            "nombre",
            "fabricante",
            "tipo_estructura",
            "soporte_motherboard",
            "precio_aproximado"
        ]
        return columnas

        