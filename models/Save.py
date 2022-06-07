from utils.db import db

class Save(db.Model):
    id_save = db.Column(db.Integer, primary_key = True)
    id_usuario = db.Column(db.Integer, nullable= False)
    nombre_motherboard = db.Column(db.String(75))
    nombre_cpu = db.Column(db.String(75))
    nombre_ram = db.Column(db.String(75))
    nombre_gpu = db.Column(db.String(75))
    nombre_almacenamiento1 = db.Column(db.String(75))
    nombre_almacenamiento2 = db.Column(db.String(75))
    nombre_fuente = db.Column(db.String(75))
    nombre_gabinete = db.Column(db.String(75))
    precio_aproximado = db.Column(db.Integer)

    def __init__(self, id_usuario, nombre_motherboard, nombre_cpu, nombre_ram, nombre_gpu, nombre_almacenamiento1, nombre_almacenamiento2, nombre_fuente, nombre_gabinete, precio_aproximado):
        self.id_usuario = id_usuario
        self.nombre_motherboard = nombre_motherboard
        self.nombre_cpu = nombre_cpu
        self.nombre_ram = nombre_ram
        self.nombre_gpu = nombre_gpu
        self.nombre_almacenamiento1 = nombre_almacenamiento1
        self.nombre_almacenamiento2 = nombre_almacenamiento2
        self.nombre_fuente = nombre_fuente
        self.nombre_gabinete = nombre_gabinete
        self.precio_aproximado = precio_aproximado