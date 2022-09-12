from flask import Flask,session,render_template
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
import os

#---------------------------------------- MODULOS ----------------------------------
from general.general import general_bp
from auth.auth import auth_bp
from builder.builder import builder_bp
from admin.admin import admin_bp

#---------------------------------------- CARGAR LAS VARIABLES PARA EL ENTORNO DE DESARROLLO ----------------------------------
from dotenv import load_dotenv
load_dotenv()

#---------------------------------------- CONFIGURACION DEL OBJETO FLASK ----------------------------------
app = Flask(__name__, template_folder='assets/templates', static_folder='assets/static')
app.secret_key = os.environ.get('APP_SECRET_KEY')

#---------------------------------------- CONFIGURACION PARA SESSION --------------------------------------
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

#--------------------------------------- CONFIGURACION PARA SQLALCHEMY/MYSQL --------------------------------------
app.config['SQLALCHEMY_DATABASE_URI']=os.environ.get('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
SQLAlchemy(app)

#--------------------------------------- REGISTRO DE BLUEPRINTS ---------------------------------------------------
app.register_blueprint(general_bp)
app.register_blueprint(auth_bp)
app.register_blueprint(builder_bp)
app.register_blueprint(admin_bp)

@app.errorhandler(404)
def page_not_found(e):
    # Esto es para el error 404
    return render_template('404.html'), 404
