#Para la creacion de la TABLA
from utils.database import Base
from sqlalchemy import  Column, Integer, String, Float
class Gpu(Base):
    __tablename__ = 'gpu'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(75), nullable= False)
    fabricante = Column(String(75), nullable= False)
    capacidad_memoria = Column(String(75), nullable= False)
    tipo_memoria = Column(String(75), nullable= False)
    potencia_tipica = Column(String(75), nullable= False)
    recomendacion_fuente = Column(String(75), nullable= False)
    interfaz_memoria = Column(String(75), nullable= False)
    precio_aproximado = Column(Integer, nullable= False)
    web = Column(String(250), nullable= False)
    rendimiento = Column(Float, nullable= False)


    def __init__(self, nombre, fabricante, capacidad_memoria, tipo_memoria, potencia_tipica, recomendacion_fuente, interfaz_memoria, precio_aproximado, web, rendimiento):
        self.nombre = nombre
        self.fabricante = fabricante
        self.capacidad_memoria = capacidad_memoria
        self.tipo_memoria = tipo_memoria
        self.potencia_tipica = potencia_tipica
        self.recomendacion_fuente = recomendacion_fuente
        self.interfaz_memoria = interfaz_memoria
        self.precio_aproximado = precio_aproximado
        self.web = web
        self.rendimiento = rendimiento

    def caracteristicas_gpu():
        caracteristicas={
            "1" : "ID",
            "2" : "Nombre",
            "3" : "Fabricante",
            "4" : "Capacidad",
            "5" : "Tipo de Memoria",
            "6" : "Consumo tipico",
            "7" : "Recomendacion PSU",
            "8" : "Interfaz Memoria",
            "9" : "Precio",
            "10" : "Opciones"
        }
        return caracteristicas

    def columnas_gpu():
        columnas = [
            "id",
            "nombre",
            "fabricante",
            "capacidad_memoria",
            "tipo_memoria",
            "potencia_tipica",
            "recomendacion_fuente",
            "interfaz_memoria",
            "precio_aproximado"
        ]
        return columnas

        

