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

@auth_bp.route('/register', methods=['POST'])
def register():
    name = request.form['name']
    email = request.form['email']
    password = request.form['pass']
    re_password = request.form['re_pass']
    admin=0
    registered_user = User.query.filter_by(email=email).first()
    alert_type="alert alert-danger"
    if password != re_password:
        flash('Las contraseñas no coinciden')
        url_chain='register.html'
    elif name=='' or email =='' or password=='':
        flash('Faltan datos')
        url_chain='register.html'
    elif registered_user and email==registered_user.email:
        flash('Usuario ya registrado')
        url_chain='register.html'
    else:
        new_user = User(email=email,nombre_cuenta=name,password=password,admin=admin)
        db.session.add(new_user)
        db.session.commit()
        db.session.close()
        url_chain='login.html'
        flash(f'Usuario {name} agregado')
        alert_type="alert alert-success"
    return render_template(url_chain, alert_type=alert_type)
        

@auth_bp.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        # Guardo lo que vino del formulario en variables
        username = request.form['mail']
        password = request.form['password']
        logged_user = User.query.filter_by(email=username).first()
        alert_type="alert alert-danger"
        if username == '':
            flash('Faltan el mail')
            url_chain='login.html'
        elif not logged_user:
            flash('No se encontro el usuario')
            url_chain='login.html'
        elif logged_user.password != password:
            flash('Contraseña incorrecta')
            url_chain='login.html'
        else:
            session['username'] = logged_user.nombre_cuenta
            message =  f"Bienvenido {logged_user.nombre_cuenta}"
            session['email'] = logged_user.email
            flash(message)
            url_chain='general/index.html'
            session['loggedin'] = True
            session['admin']= logged_user.admin
            session['armador_manual'] = {}
        return render_template(url_chain,alert_type=alert_type)

@auth_bp.route('/logout')
def logout():
    # Para elminar los datos del diccionario session
    message = f"Hasta Luego {session['username']}"
    session.clear()
    # Renderiza la ruta principal
    flash(message)
    return redirect(url_for('general.Index'))