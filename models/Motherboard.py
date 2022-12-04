#Para la creacion de la TABLA
from utils.database import Base
from sqlalchemy import  Column, Integer, String

class Motherboard(Base):
    __tablename__ = 'motherboard'
    id = Column(Integer, primary_key=True, nullable= False)
    nombre = Column(String(75), nullable= False)
    fabricante = Column(String(75), nullable= False)
    zocalo = Column(String(75), nullable= False)
    chipset = Column(String(75), nullable= False)
    soporte_memoria = Column(String(75), nullable= False)
    factor_forma = Column(String(75), nullable=False)
    precio_aproximado= Column(Integer, nullable= False)
    web = Column(String(250), nullable= False)

    def __init__(self, nombre, fabricante, zocalo, chipset, soporte_memoria, factor_forma, precio_aproximado, web):
        self.nombre = nombre
        self.fabricante = fabricante
        self.zocalo = zocalo
        self.chipset = chipset
        self.soporte_memoria = soporte_memoria
        self.factor_forma = factor_forma
        self.precio_aproximado = precio_aproximado
        self.web = web

    def caracteristicas_motherboard():
        caracteristicas={
            "1" : "ID",
            "2" : "Nombre",
            "3" : "Fabricante",
            "4" : "Zocalo",
            "5" : "Soporte Memoria",
            "6" : "Precio Aproximado",
            "7" : "Opciones"
        }
        return caracteristicas

    def columnas_motherboard():
        columnas = [
            "id",
            "nombre",
            "fabricante",
            "zocalo",
            "soporte_memoria",
            "precio_aproximado",
        ]
        return columnas
