from utils.db import db

class Gpu(db.Model):

    id_gpu = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(75), nullable= False)
    fabricante = db.Column(db.String(75), nullable= False)
    capacidad_memoria = db.Column(db.String(75), nullable= False)
    tipo_memoria = db.Column(db.String(75), nullable= False)
    potencia_tipica = db.Column(db.String(75), nullable= False)
    recomendacion_fuente = db.Column(db.String(75), nullable= False)
    interfaz_memoria = db.Column(db.String(75), nullable= False)
    precio_aproximado = db.Column(db.Integer, nullable= False)
    web = db.Column(db.String(250), nullable= False)
    rendimiento = db.Column(db.Float, nullable= False)


    def __init__(self, nombre, fabricante, capacidad_memoria, tipo_memoria, potencia_tipica, recomendacion_fuente, interfaz_memoria, precio_aproximado, web, rendimiento):
        self.nombre = nombre
        self.fabricante = fabricante
        self.capacidad_memoria = capacidad_memoria
        self.tipo_memoria = tipo_memoria
        self.potencia_tipica = potencia_tipica
        self.recomendacion_fuente = recomendacion_fuente
        self.interfaz_memoria = interfaz_memoria
        self.precio_aproximado = precio_aproximado
        self.web = web
        self.rendimiento = rendimiento