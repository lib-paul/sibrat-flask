from utils.db import db

class Fuente(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable= False)
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


    def caracteristicas_fuente():
        caracteristicas={
            "1" : "ID",
            "2" : "Nombre",
            "3" : "Fabricante",
            "4" : "Certificación",
            "5" : "Potencia de salida",
            "6" : "Tipo de fuente",
            "7" : "Corrector de potencia",
            "8" : "Precio",
            "9" : "Opciones"
        }
        return caracteristicas

    def columnas_fuente():
        columnas = [
            "id",
            "nombre",
            "fabricante",
            "certificacion",
            "potencia_salida",
            "tipo_fuente",
            "corrector_fpotencia",
            "precio_aproximado"
        ]
        return columnas

        