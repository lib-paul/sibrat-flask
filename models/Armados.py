#Para la creacion de la TABLA
from utils.database import Base
from sqlalchemy.orm import relationship, backref
from sqlalchemy import Column, Integer, String, ForeignKey

class Armados(Base):
    __tablename__ = 'armados'
    id = Column(Integer, primary_key= True, nullable = False)
    nombre_motherboard = Column(String(75), nullable= False)
    nombre_cpu = Column(String(75), nullable= False)
    nombre_ram = Column(String(75), nullable= False)
    cant_ram = Column(Integer)
    nombre_gpu = Column(String(75), nullable= False)
    nombre_alm_principal = Column(String(75), nullable= False)
    nombre_alm_secundario =Column(String(75), nullable= False)
    nombre_fuente = Column(String(75), nullable= False)
    precio_total =Column(Integer)
    tipo_armados = Column(Integer,ForeignKey('tipo_armado.id'))
    id_usuario = Column(Integer,ForeignKey('user.id'))

    def __init__(self,nombre_motherboard,nombre_cpu,nombre_ram,cant_ram,nombre_gpu, nombre_alm_principal,nombre_alm_secundario,nombre_fuente,precio_total,tipo_armados):
        self.nombre_motherboard = nombre_motherboard
        self.nombre_cpu = nombre_cpu
        self.nombre_ram = nombre_ram
        self.cant_ram = cant_ram
        self.nombre_gpu = nombre_gpu
        self.nombre_alm_principal = nombre_alm_principal
        self.nombre_alm_secundario = nombre_alm_secundario
        self.nombre_fuente = nombre_fuente
        self.precio_total = precio_total
        self.tipo_armados = tipo_armados

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

class TipoArmado(Base):
    __tablename__ = 'tipo_armado'
    id = Column(Integer, primary_key=True, nullable=False)
    tipo = Column(String(75), nullable=False)
    tipo_armados = relationship('Armados', backref='tipo_armado')

    def __init__(self,tipo):
        self.tipo= tipo
    
    def __str__(self) -> str:
        return self.tipo