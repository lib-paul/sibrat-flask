from utils.db import db

class Fuente(db.Model):
    id_fuente = db.Column(db.Integer, primary_key=True, nullable= False)
    nombre = db.Column(db.String(75), nullable= False)
    fabricante = db.Column(db.String(75), nullable= False)
    certificacion = db.Column(db.String(75), nullable= False)
    potencia_salida = db.Column(db.String(75), nullable= False)
    tipo_fuente = db.Column(db.String(75), nullable= False)
    corrector_fpotencia= db.Column(db.String(75), nullable= False)
    precio_aproximado = db.Column(db.Integer, nullable= False)
    web = db.Column(db.String(250), nullable= False)

    def __init__(self, nombre, fabricante, certificacion, potencia_salida, tipo_fuente, corrector_fpotencia, precio_aproximado, web):
        self.nombre = nombre
        self.fabricante = fabricante
        self.certificacion = certificacion
        self.potencia_salida = potencia_salida
        self.tipo_fuente = tipo_fuente
        self.corrector_fpotencia = corrector_fpotencia
        self.precio_aproximado = precio_aproximado
        self.web = web