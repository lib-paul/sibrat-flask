from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from utils.imports_admin import *
from utils.database import db_session as db
from flask_security import auth_required


recommender_bp = Blueprint('recommender', __name__, template_folder="templates")

@recommender_bp.route('/recomendador')
@auth_required()
def recomendador_inicio():
    return render_template('start.html')

@recommender_bp.route('/recomendador/computadoras')
@auth_required()
def recomendar_computadora_view():
    preguntas = Pregunta.query.all()
    respuestas = Respuesta.query.all()
    db.close()
    return render_template('form_computadora.html',preguntas = preguntas, respuestas=respuestas)

@recommender_bp.route('/formulario_computadora', methods=['POST'])
@auth_required()
def recomendar_computadora():
    print('llegue')
    lista = request.form 
    print(lista)
    return render_template('start.html')

   