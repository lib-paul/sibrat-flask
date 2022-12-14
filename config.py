#FLASK
from flask import Flask,session,render_template,url_for,redirect,request
from flask_session import Session

#FLASK-ADMIN
from flask_admin.contrib.sqla import ModelView  
from flask_admin.menu import MenuLink
from flask_admin import Admin
from flask_admin import AdminIndexView

#FLASK-SECURITY
from flask_security import Security, current_user, \
    SQLAlchemySessionUserDatastore, LoginForm, \
    url_for_security, current_user, auth_required, RegisterForm, ResetPasswordForm, ForgotPasswordForm
from flask_security.views import login, register

#FLASK-MAIL
from flask_mailman import Mail

#OTHERS
import os
from utils.database import init_db, db_session as db
from utils.imports_admin import *


#---------------------------------------- MODULOS/Blueprints ----------------------------------
from general.general import general_bp
from builder.builder import builder_bp
from recommender.recommender import recommender_bp

#---------------------------------------- CARGAR LAS VARIABLES PARA EL ENTORNO DE DESARROLLO ----------------------------------
from dotenv import load_dotenv
load_dotenv()

#---------------------------------------- CONFIGURACION DEL OBJETO FLASK ----------------------------------
app = Flask(__name__, template_folder='assets/templates', static_folder='assets/static')
app.config['SECURITY_PASSWORD_SALT'] = os.environ.get('SECURITY_PASSWORD_SALT')
app.config['SECRET_KEY'] = os.environ.get('APP_SECRET_KEY')
app.config["VERSION"] = "SIBRAT Main v0.8"
app.config["VERSION_ADMIN"] = "SIBRAT Admin v0.5"
app.config["APP_COLOR_MODE"] = "dark"
app.config["APP_TEXT_COLOR_MODE"] ="white"
app.config['SECURITY_REGISTERABLE'] = True
app.config['SECURITY_CONFIRMABLE'] = True
app.config['SECURITY_RECOVERABLE'] = True
app.config['SECURITY_CHANGEABLE'] = True
app.config['SECURITY_TRACKABLE'] = True
app.config['SECURITY_USERNAME_ENABLE'] = True
app.config['SECURITY_USERNAME_REQUIRED'] = True
app.jinja_env.filters['zip'] = zip

#---------------------------------------- CONFIGURACION PARA SESSION --------------------------------------
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
Session(app)





#--------------------------------------- CONFIGURACION SECURITY ---------------------------------------------------
user_datastore = SQLAlchemySessionUserDatastore(db, User, Role)
app.security = Security(app, user_datastore)

#Defino el contexto para los login y register custom esto les permite recibir las validaciones hechas en flask-wtf
@app.context_processor
def login_context():
    return {
        'url_for_security': url_for_security,
        'login_user_form': LoginForm(),
    }
def register_context():
    return {
        'url_for_security': url_for_security,
        'register_user_form': RegisterForm(),
    }
def reset_password_context():
    return {
        'url_for_security': url_for_security,
        'forgot_password_form': ForgotPasswordForm(),
        'reset_password_form': ResetPasswordForm(),
    }
def forgot_password_context():
    return {
        'url_for_security': url_for_security,
        'forgot_password_form': ForgotPasswordForm(),
        'reset_password_form': ResetPasswordForm(),
    }
    
#--------------------------------------- CONFIGURACION MAILS -----------------------------------------------------
app.config['MAIL_SERVER']=os.environ.get('MAIL_SERVER')
app.config['MAIL_PORT'] = os.environ.get('MAIL_PORT')
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')
app.config['MAIL_USE_TLS'] = os.environ.get('MAIL_USE_TLS')
app.config['MAIL_USE_SSL'] = False
mail = Mail(app)
#--------------------------------------- REGISTRO DE BLUEPRINTS ---------------------------------------------------

app.register_blueprint(general_bp)
app.register_blueprint(builder_bp)
app.register_blueprint(recommender_bp)

#--------------------------------------- CONFIGURACION PARA EL MODULO DE ADMIN ---------------------------------------------------
class HomeAdminView(AdminIndexView):
    def is_accessible(self):
        if not current_user.is_anonymous:
            return current_user.has_role('Administrador') or current_user.has_role('Tecnico1') or current_user.has_role('Tecnico2')
        else:
            return False

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('general.Index'))

app.config['FLASK_ADMIN_SWATCH']="darkly"
app.config['FLASK_ADMIN_FLUID_LAYOUT']= True
admin = Admin(app, name=app.config["VERSION_ADMIN"] ,template_mode="bootstrap4", url="/admin", index_view=HomeAdminView(name="Home"))


class ModeloAdmin(ModelView):
    create_modal = True
    edit_modal = True
    def is_accessible(self):
        if not current_user.is_anonymous:
            return current_user.has_role('Administrador') 
        else:
            return False
    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('general.Index'))    

class ModeloAdminUser(ModeloAdmin):
    column_searchable_list = ['username']
    column_exclude_list = ['password']
    form_excluded_columns = ['password', 'fs_uniquifier', 'login_count' , 'confirmed_at' , 'last_login_ip', 'current_login_ip', 'last_login_at' , 'current_login_at']

class ModeloTecnico1(ModelView):
    create_modal = True
    edit_modal = True
    def is_accessible(self):
        if not current_user.is_anonymous:
            return current_user.has_role('Administrador') or current_user.has_role('Tecnico1')
        else:
            return False
    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('general.Index'))   

class ModeloTecnico2(ModelView):
    create_modal = True
    edit_modal = True
    def is_accessible(self):
        if not current_user.is_anonymous:
            return current_user.has_role('Administrador') or current_user.has_role('Tecnico1') or current_user.has_role('Tecnico2')
        else:
            return False
    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('general.Index'))   

#MODELOS PARA USUARIOS (PERMISO NECESARIO "ADMIN")
admin.add_view(ModeloAdminUser(User,db, category="Usuarios"))
admin.add_view(ModeloAdmin(Role,db, category="Usuarios"))
admin.add_view(ModeloAdmin(RolesUsers,db, category="Usuarios"))
admin.add_view(ModeloAdmin(Tecnico,db, category="Usuarios"))
#MODELOS PARA LOS COMPONENTES (PERMISO NECESARIO "ADMIN" O "TECNICO" NIVEL 1)
admin.add_view(ModeloTecnico1(Cpu,db,category="Componentes"))
admin.add_view(ModeloTecnico1(Gpu,db,category="Componentes"))
admin.add_view(ModeloTecnico1(Motherboard,db,category="Componentes"))
admin.add_view(ModeloTecnico1(Ram,db,category="Componentes"))
admin.add_view(ModeloTecnico1(Almacenamiento,db,category="Componentes"))
admin.add_view(ModeloTecnico1(Fuente,db,category="Componentes"))
admin.add_view(ModeloTecnico1(Gabinete,db,category="Componentes"))
#MODELOS DEL RECOMENDADOR (PERMISO NECESARIO "ADMIN" O "TECNICO" NIVEL 1 O 2)
admin.add_view(ModeloTecnico2(Pregunta,db,category="Recomendador"))
admin.add_view(ModeloTecnico2(Respuesta,db,category="Recomendador"))
admin.add_view(ModeloTecnico2(TipoPregunta,db,category="Recomendador"))
# MODELOS DEL SISTEMA (PERMISO NECESARIO "ADMIN")
admin.add_view(ModeloAdmin(Faq,db,category="Sistema"))
admin.add_view(ModeloAdmin(Armados,db,category="Sistema"))
admin.add_view(ModeloAdmin(TipoArmado,db,category="Sistema"))

#Simple Link en el navbar
admin.add_link(MenuLink(name="Salir del Administrador",url="/"))


#--------------------------------------- MANEJO DE ERRORES ---------------------------------------------------
@app.errorhandler(404)
def page_not_found(e):
    # Esto es para el error 404
    return render_template('404.html'), 404


#--------------------------------------- MODO OSCURO ---------------------------------------------------
@app.route('/mode-change')
def mode_switch():
    last_route = request.referrer
    print(last_route)
    if app.config["APP_COLOR_MODE"] == "dark":
        app.config["APP_COLOR_MODE"] = "light"
    else:
        app.config["APP_COLOR_MODE"] = "dark"
    return redirect(last_route)





