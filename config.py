from flask import Flask,session
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
from general.general import general_bp
from auth.auth import auth_bp
from builder.builder import builder_bp

#---------------------------------------- CONFIGURACION DEL OBJETO FLASK ----------------------------------
app = Flask(__name__, template_folder='assets/templates', static_folder='assets/static')
app.secret_key = 'A0AKR5TGD\ R~XHH!jmN]LWDSd2xXxasZz1fX/,?RT'

#---------------------------------------- CONFIGURACION PARA SESSION --------------------------------------
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"

Session(app)

#--------------------------------------- CONFIGURACION PARA SQLALCHEMY/MYSQL --------------------------------------
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://kgkfcgbzmdfbmc:aff925396ee9ce159c5c9c542d6e675fb04f94de74b7a36b811abec3d8886963@ec2-34-207-12-160.compute-1.amazonaws.com:5432/ddc6481874p72a'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
SQLAlchemy(app)

#--------------------------------------- REGISTRO DE BLUEPRINTS ---------------------------------------------------
app.register_blueprint(general_bp)
app.register_blueprint(auth_bp)
app.register_blueprint(builder_bp)

