#Para la creacion de la TABLA
from utils.database import Base
from sqlalchemy import  Column, Integer, String

class Cpu(Base):
    __tablename__ = 'cpu'
    id = Column(Integer, primary_key=True, nullable= False)
    id_integrada = Column(Integer)
    nombre = Column(String(75), nullable= False)
    fabricante = Column(String(75), nullable= False)
    litografia = Column(String(75), nullable= False)
    frecuencia_max = Column(String(75), nullable= False)
    tdp = Column(String(75), nullable= False)
    soporte_memoria = Column(String(75), nullable= False)
    zocalo = Column(String(75), nullable= False)
    precio_aproximado = Column(Integer, nullable= False)
    web = Column(String(250), nullable= False)

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

    def caracteristicas_cpu():
        caracteristicas={
            "1" : "ID",
            "2" : "Nombre",
            "3" : "Fabricante",
            "4" : "Litografia",
            "5" : "Frecuencia Maxima",
            "6" : "TDP",
            "7" : "Soporte Memoria",
            "8" : "Socket",
            "9" : "Precio",
            "10" : "Opciones"
        }
        return caracteristicas

    def columnas_cpu():
        columnas = [
            "id",
            "nombre",
            "fabricante",
            "litografia",
            "frecuencia_max",
            "tdp",
            "soporte_memoria",
            "zocalo",
            "precio_aproximado"
        ]
        return columnas