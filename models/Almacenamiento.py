import imp
from utils.db import db

class Almacenamiento(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable= False)
    nombre = db.Column(db.String(75), nullable= False)
    fabricante = db.Column(db.String(75), nullable= False)
    capacidad = db.Column(db.String(75), nullable= False)
    tecnologia_almacenamiento = db.Column(db.String(75), nullable= False)
    interfaz = db.Column(db.String(75), nullable= False)
    factor_forma = db.Column(db.String(75), nullable= False)
    precio_aproximado = db.Column(db.Integer, nullable= False)
    web = db.Column(db.String(250), nullable= False)

    def __init__(self, nombre, fabricante, capacidad, tecnologia_almacenamiento, interfaz, factor_forma, precio_aproximado, web):
        self.nombre = nombre
        self.fabricante = fabricante
        self.capacidad = capacidad
        self.tecnologia_almacenamiento = tecnologia_almacenamiento
        self.interfaz = interfaz
        self.factor_forma = factor_forma
        self.precio_aproximado = precio_aproximado
        self.web = web

    def caracteristicas_almacenamiento():
        caracteristicas={
            "1" : "ID",
            "2" : "Nombre",
            "3" : "Fabricante",
            "4" : "Capacidad",
            "5" : "Tecnologia",
            "6" : "Interfaz",
            "7" : "Factor forma",
            "8" : "Precio",
            "9" : "Opciones"
        }
        return caracteristicas

    def columnas_almacenamiento():
        columnas = [
            "id",
            "nombre",
            "fabricante",
            "capacidad",
            "tecnologia_almacenamiento",
            "interfaz",
            "factor_forma",
            "precio_aproximado"
        ]
        return columnas