#Para la creacion de la TABLA
from utils.database import Base
from sqlalchemy.orm import relationship, backref
from sqlalchemy import  Column, Integer, String, ForeignKey, Text

class Pregunta(Base):
    __tablename__ = 'pregunta'
    id = Column(Integer, primary_key=True, nullable= False)
    titulo = Column(String(75), nullable= False)
    enunciado = Column(Text, nullable = False)

    #Relacion con respuesta
    respuestas = relationship('Respuesta', backref='pregunta')

    #Id del tipo de pregunta
    #tipo_id = Column(Integer,ForeignKey('tipo_pregunta.id'))

    def __init__(self, titulo, enunciado):
        self.titulo= titulo
        self.enunciado = enunciado

    def __unicode__(self):
        return self.titulo
    def __str__(self):
        return self.titulo


class Respuesta(Base):
    __tablename__ = 'respuesta'
    id = Column(Integer, primary_key=True, nullable= False)
    respuesta = Column(String(75), nullable= False)
    val_cpu = Column(Integer, nullable= False)
    val_gpu = Column(Integer, nullable = False)
    val_ram = Column(Integer, nullable = False)
    val_almacenamiento = Column(Integer, nullable = False)
    pregunta_id = Column(Integer,ForeignKey('pregunta.id'))

    def __init__(self, respuesta, val_cpu, val_gpu, val_ram, val_almacenamiento):
        self.respuesta = respuesta
        self.val_cpu = val_cpu
        self.val_gpu = val_gpu
        self.val_ram = val_ram
        self.val_almacenamiento = val_almacenamiento


class TipoPregunta(Base):
    __tablename__ = 'tipo_respuesta'
    id = Column(Integer, primary_key=True, nullable= False)
    tipo = Column(String(75), nullable= False)
    #tipo_pregunta = relationship('Pregunta', backref='tipo_pregunta')

    def __init__(self, tipo):
        self.tipo = tipo
    
    def __unicode__(self):
        return self.tipo

    def __str__(self):
        return self.tipo

