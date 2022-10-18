from utils.imports_config import *
from utils.imports_admin import *
import os

#---------------------------------------- MODULOS/Blueprints ----------------------------------
from general.general import general_bp
from auth.auth import auth_bp
from builder.builder import builder_bp

#---------------------------------------- CARGAR LAS VARIABLES PARA EL ENTORNO DE DESARROLLO ----------------------------------
from dotenv import load_dotenv
load_dotenv()

#---------------------------------------- CONFIGURACION DEL OBJETO FLASK ----------------------------------
app = Flask(__name__, template_folder='assets/templates', static_folder='assets/static')
app.secret_key = os.environ.get('APP_SECRET_KEY')
app.config["VERSION"] = "SIBRAT Main v0.7"
app.config["VERSION_ADMIN"] = "SIBRAT Admin v0.3"
app.config["APP_COLOR_MODE"] = "dark"
app.config["APP_TEXT_COLOR_MODE"] ="white"
app.jinja_env.filters['zip'] = zip
#---------------------------------------- CONFIGURACION PARA SESSION --------------------------------------
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

#--------------------------------------- CONFIGURACION PARA SQLALCHEMY/MYSQL/POSGRESQL --------------------------------------
app.config['SQLALCHEMY_DATABASE_URI']=os.environ.get('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
SQLAlchemy(app)

#--------------------------------------- REGISTRO DE BLUEPRINTS ---------------------------------------------------
app.register_blueprint(general_bp)
app.register_blueprint(auth_bp)
app.register_blueprint(builder_bp)

#--------------------------------------- CONFIGURACION PARA EL MODULO DE ADMIN ---------------------------------------------------
app.config['FLASK_ADMIN_SWATCH']="darkly"
app.config['FLASK_ADMIN_FLUID_LAYOUT']= True
admin = Admin(app, name=app.config["VERSION_ADMIN"] ,template_mode="bootstrap4")

#ModelView agrega al navbar las opciones para el ABM
admin.add_view(ModelView(User,db.session))
admin.add_view(ModelView(Cpu,db.session))
admin.add_view(ModelView(Gpu,db.session))
admin.add_view(ModelView(Motherboard,db.session))
admin.add_view(ModelView(Ram,db.session))
admin.add_view(ModelView(Almacenamiento,db.session))
admin.add_view(ModelView(Fuente,db.session))
admin.add_view(ModelView(Gabinete,db.session))

#Simple Link en el navbar
admin.add_link(MenuLink(name="Main",url="/"))

#--------------------------------------- MANEJO DE ERRORES ---------------------------------------------------
@app.errorhandler(404)
def page_not_found(e):
    # Esto es para el error 404
    return render_template('404.html'), 404


@app.route('/mode-swith')
def mode_switch():
    if app.config["APP_COLOR_MODE"] == "dark":
        app.config["APP_COLOR_MODE"] = "light"
    else:
        app.config["APP_COLOR_MODE"] = "dark"
    return render_template('general/index.html')