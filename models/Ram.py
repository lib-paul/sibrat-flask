#Para la creacion de la TABLA
from utils.database import Base
from sqlalchemy import  Column, Integer, String, ForeignKey
class Ram(Base):
    __tablename__ = 'ram'
    id = Column(Integer, primary_key=True , nullable = False)
    nombre = Column(String(75), nullable = False)
    fabricante = Column(String(75), nullable = False)
    capacidad = Column(String(75), nullable = False)
    velocidad = Column(String(75), nullable = False)
    formato = Column(String(75), nullable = False)
    tipo = Column(String(75), nullable = False)
    precio_aproximado = Column(Integer, nullable = False)
    web = Column(String(250), nullable = False)

    def __init__(self, nombre, fabricante, capacidad, velocidad, formato, tipo, precio_aproximado, web):
        self.nombre = nombre
        self.fabricante = fabricante
        self.capacidad = capacidad
        self.velocidad = velocidad
        self.formato = formato
        self.tipo = tipo
        self.precio_aproximado = precio_aproximado
        self.web = web

    def caracteristicas_ram():
        caracteristicas={
            "1" : "ID",
            "2" : "Nombre",
            "3" : "Fabricante",
            "4" : "Capacidad",
            "5" : "Velocidad",
            "6" : "Tipo",
            "7" : "Precio",
            "8" : "Opciones"
        }
        return caracteristicas

    def columnas_ram():
        columnas = [
            "id",
            "nombre",
            "fabricante",
            "capacidad",
            "velocidad",
            "tipo",
            "precio_aproximado"
        ]
        return columnas