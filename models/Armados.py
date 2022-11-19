from utils.db import db

class Armados(db.Model):
    id = db.Column(db.Integer, primary_key= True, nullable = False)
    nombre_motherboard = db.Column(db.String(75), nullable= False)
    nombre_cpu = db.Column(db.String(75), nullable= False)
    nombre_ram = db.Column(db.String(75), nullable= False)
    cant_ram = db.Column(db.Integer)
    nombre_gpu = db.Column(db.String(75), nullable= False)
    nombre_alm_principal = db.Column(db.String(75), nullable= False)
    nombre_alm_secundario =db.Column(db.String(75), nullable= False)
    nombre_fuente = db.Column(db.String(75), nullable= False)
    precio_total =db.Column(db.Integer)
    tipo_armado = db.Column(db.String(75), nullable= False)

    def __init__(self,nombre_motherboard,nombre_cpu,nombre_ram,cant_ram,nombre_gpu, nombre_alm_principal,nombre_alm_secundario,nombre_fuente,precio_total,tipo_armado):
        self.nombre_motherboard = nombre_motherboard
        self.nombre_cpu = nombre_cpu
        self.nombre_ram = nombre_ram
        self.cant_ram = cant_ram
        self.nombre_gpu = nombre_gpu
        self.nombre_alm_principal = nombre_alm_principal
        self.nombre_alm_secundario = nombre_alm_secundario
        self.nombre_fuente = nombre_fuente
        self.precio_total = precio_total
        self.tipo_armado = tipo_armado

    def caracteristicas_armado():
        caracteristicas={
            "1" : "Armado N°",
            "2" : "Motherboard",
            "3" : "CPU",
            "4" : "RAM",
            "5" : "Cantidad de Ram",
            "6" : "GPU",
            "7" : "Almacenamiento 1",
            "8" : "Almacenamiento 2",
            "9" : "Fuente",
            "10" : "Total Aproximado"
        }
        return caracteristicas

    def columnas_armado():
        columnas=[
            "id",
            "nombre_motherboard",
            "nombre_cpu",
            "nombre_ram",
            "cant_ram",
            "nombre_gpu",
            "nombre_alm_principal",
            "nombre_alm_secundario",
            "nombre_fuente"
            "precio_total"
        ]
        return columnas