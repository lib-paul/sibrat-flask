#Para la creacion de la TABLA
from utils.database import Base
from sqlalchemy import  Column, Integer, String, Float

class CpuIntegrada(Base):
    __tablename__ = 'cpu_integrada'
    id_cpuIntegrada = Column(Integer, primary_key=True, nullable=False)
    nombre = Column(String(75), nullable=False)
    frecuencia_max = Column(String(75), nullable=False)
    interfaz_memoria = Column(String(75), nullable=False)
    #A este modelo le falta precio_aproximado.
    web = Column(String(250), nullable=False)
    rendimiento = Column(Float, nullable=False)

    def __init__(self, nombre, frecuencia_max, interfaz_memoria, web, rendimiento):
        self.nombre = nombre
        self.frecuencia_max = frecuencia_max
        self.interfaz_memoria = interfaz_memoria
        self.web = web
        self.rendimiento = rendimiento
