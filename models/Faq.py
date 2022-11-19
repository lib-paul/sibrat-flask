from utils.db import db

class Faq(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(75), nullable =False)
    descripcion = db.Column(db.Text, nullable= False) 

    def __init__(self, titulo, descripcion):
        self.titulo = titulo
        self.descripcion = descripcion