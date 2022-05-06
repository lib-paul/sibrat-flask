import email
from email import message
from flask import Blueprint, render_template, request, redirect, url_for,session,flash
from models.User import User
from utils.db import db

auth_bp = Blueprint('auth',__name__,template_folder='templates')

@auth_bp.route('/iniciar-sesion')
def loguearse_vista():
    
    return render_template('login.html')

@auth_bp.route('/registrarse')
def registrarse_vista():
    return render_template('register.html')

@auth_bp.route('/register')
def register():
    
        

@auth_bp.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        # Guardo lo que vino del formulario en variables
        username = request.form['mail']
        password = request.form['password']
        logged_user = User.query.filter_by(email=username).first()
        if username == '':
            flash('Faltan el mail')
            url_chain='auth.loguearse_vista'
        elif not logged_user:
            flash('No se encontro el usuario')
            url_chain='auth.loguearse_vista'
        elif logged_user.password != password:
            flash('Contraseña incorrecta')
            url_chain='auth.loguearse_vista'
        else:
            session['username'] = logged_user.nombre_cuenta
            message =  f"Bienvenido {logged_user.nombre_cuenta}"
            flash(message)
            url_chain='general.Index'
        return redirect(url_for(url_chain))

@auth_bp.route('/logout')
def logout():
    # Para elminar los datos del diccionario session
    message = f"Hasta Luego {session['username']}"
    session.clear()
    # Renderiza la ruta principal
    flash(message)
    return redirect(url_for('general.Index'))