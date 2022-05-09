from socket import socket
from utils.db import db

class Cpu(db.Model):
    id_cpu = db.Column(db.Integer, primary_key=True, nullable= False)
    id_integrada = db.Column(db.Integer, nullable= False)
    nombre = db.Column(db.Strig(75), nullable= False)
    fabricante = db.Column(db.Strig(75), nullable= False)
    litografia = db.Column(db.Strig(75), nullable= False)
    frecuencia_max = db.Column(db.Strig(75), nullable= False)
    tdp = db.Column(db.Strig(75), nullable= False)
    soporte_memoria = db.Column(db.Strig(75), nullable= False)
    zocalo = db.Column(db.Strig(75), nullable= False)
    precio_aproximado = db.Column(db.Integer, nullable= False)
    web = db.Column(db.Strig(250), nullable= False)

    def __init__(self, nombre, fabricante, litografia, frecuencia_max, tdp, soporte_memoria, zocalo, precio_aproximado, web):
        self.nombre = nombre
        self.fabricante = fabricante
        self.litografia = litografia
        self.frecuencia_max = frecuencia_max
        self.tdp = tdp
        self.soporte_memoria = soporte_memoria
        self.zocalo = zocalo
        self.precio_aproximado = precio_aproximado
        self.web = web