from utils.db import db

class Pregunta(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable= False)
    titulo = db.Column(db.String(75), nullable= False)
    enunciado = db.Column(db.Text, nullable = False)

    #Relacion con respuesta
    respuestas = db.relationship('Respuesta', backref='pregunta')

    #Id del tipo de pregunta
    tipo_id = db.Column(db.Integer,db.ForeignKey('tipo_pregunta.id'))

    def __init__(self, titulo, enunciado):
        self.titulo= titulo
        self.enunciado = enunciado

    def __unicode__(self):
        return self.titulo
    def __str__(self):
        return self.titulo


class Respuesta(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable= False)
    respuesta = db.Column(db.String(75), nullable= False)
    val_cpu = db.Column(db.Integer, nullable= False)
    val_gpu = db.Column(db.Integer, nullable = False)
    val_ram = db.Column(db.Integer, nullable = False)
    val_almacenamiento = db.Column(db.Integer, nullable = False)
    pregunta_id = db.Column(db.Integer,db.ForeignKey('pregunta.id'))

    def __init__(self, respuesta, val_cpu, val_gpu, val_ram, val_almacenamiento):
        self.respuesta = respuesta
        self.val_cpu = val_cpu
        self.val_gpu = val_gpu
        self.val_ram = val_ram
        self.val_almacenamiento = val_almacenamiento


class TipoPregunta(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable= False)
    tipo = db.Column(db.String(75), nullable= False)
    tipo_pregunta = db.relationship('Pregunta', backref='tipopregunta')

    def __init__(self, tipo):
        self.tipo = tipo
    
    def __unicode__(self):
        return self.tipo

    def __str__(self):
        return self.tipo

