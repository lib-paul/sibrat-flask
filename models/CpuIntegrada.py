from utils.db import db

class CpuIntegrada(db.Model):
    
    id_cpuIntegrada = db.Column(db.Integer, primary_key=True, nullable=False)
    nombre = db.Column(db.String(75), nullable=False)
    frecuencia_max = db.Column(db.String(75), nullable=False)
    interfaz_memoria = db.Column(db.String(75), nullable=False)
    #A este modelo le falta precio_aproximado.
    web = db.Column(db.String(250), nullable=False)
    rendimiento = db.Column(db.Float, nullable=False)

    def __init__(self, nombre, frecuencia_max, interfaz_memoria, web, rendimiento):
        self.nombre = nombre
        self.frecuencia_max = frecuencia_max
        self.interfaz_memoria = interfaz_memoria
        self.web = web
        self.rendimiento = rendimiento
