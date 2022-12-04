#Para la creacion de la TABLA
from utils.database import Base
from sqlalchemy import Column, Integer, String

class Almacenamiento(Base):
    __tablename__ = 'almacenamiento'
    id = Column(Integer, primary_key=True, nullable= False)
    nombre = Column(String(75), nullable= False)
    fabricante = Column(String(75), nullable= False)
    capacidad = Column(String(75), nullable= False)
    tecnologia_almacenamiento = Column(String(75), nullable= False)
    interfaz = Column(String(75), nullable= False)
    factor_forma = Column(String(75), nullable= False)
    precio_aproximado = Column(Integer, nullable= False)
    web = Column(String(250), nullable= False)

    def __init__(self, nombre, fabricante, capacidad, tecnologia_almacenamiento, interfaz, factor_forma, precio_aproximado, web):
        self.nombre = nombre
        self.fabricante = fabricante
        self.capacidad = capacidad
        self.tecnologia_almacenamiento = tecnologia_almacenamiento
        self.interfaz = interfaz
        self.factor_forma = factor_forma
        self.precio_aproximado = precio_aproximado
        self.web = web

    def caracteristicas_almacenamiento():
        caracteristicas={
            "1" : "ID",
            "2" : "Nombre",
            "3" : "Fabricante",
            "4" : "Capacidad",
            "5" : "Tecnologia",
            "6" : "Interfaz",
            "7" : "Factor forma",
            "8" : "Precio",
            "9" : "Opciones"
        }
        return caracteristicas

    def columnas_almacenamiento():
        columnas = [
            "id",
            "nombre",
            "fabricante",
            "capacidad",
            "tecnologia_almacenamiento",
            "interfaz",
            "factor_forma",
            "precio_aproximado"
        ]
        return columnas