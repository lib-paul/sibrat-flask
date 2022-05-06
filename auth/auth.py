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


@auth_bp.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        # Guardo lo que vino del formulario en variables
        username = request.form['username']
        password = request.form['password']
        logged_user = User.query.filter_by(email=username).first()
        if username == '':
            flash('Faltan el mail')
        elif not logged_user:
            flash('No se encontro el usuario')
        elif logged_user.password != password:
            flash('Contraseña incorrecta')
        
    session['username'] = logged_user.nombre_cuenta
    return redirect(url_for('general.Index'))