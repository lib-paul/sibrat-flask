#Para crear la TABLA
from utils.database import Base
from sqlalchemy import Column, Integer, String, Text
class Faq(Base):
    __tablename__ = 'faq'
    id = Column(Integer, primary_key=True)
    titulo = Column(String(75), nullable =False)
    descripcion = Column(Text, nullable= False) 

    def __init__(self, titulo, descripcion):
        self.titulo = titulo
        self.descripcion = descripcion