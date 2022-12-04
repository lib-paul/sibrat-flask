#Para la creacion de la TABLA
from utils.database import Base
from sqlalchemy import  Column, Integer, String
class Gabinete(Base):
    __tablename__ = 'gabinete'
    id = Column(Integer, primary_key=True, nullable= False)
    nombre = Column(String(75), nullable= False)
    fabricante = Column(String(75), nullable= False)
    tipo_estructura = Column(String(75), nullable= False)
    soporte_motherboard = Column(String(75), nullable= False)
    precio_aproximado = Column(Integer, nullable= False)
    web = Column(String(250), nullable= False)

    def __init__(self, nombre, fabricante, tipo_estructura, soporte_motherboard, precio_aproximado, web):
        self.nombre = nombre
        self.fabricante = fabricante
        self.tipo_estructura = tipo_estructura
        self.soporte_motherboard = soporte_motherboard
        self.precio_aproximado = precio_aproximado
        self.web = web


    def caracteristicas_gabinete():
        caracteristicas={
            "1" : "ID",
            "2" : "Nombre",
            "3" : "Fabricante",
            "4" : "Estructura",
            "5" : "Soporte MB",
            "6" : "Precio",
            "7" : "Opciones"
        }
        return caracteristicas

    def columnas_gabinete():
        columnas = [
            "id",
            "nombre",
            "fabricante",
            "tipo_estructura",
            "soporte_motherboard",
            "precio_aproximado"
        ]
        return columnas

        