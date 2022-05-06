from flask import Flask
from general.general import general_bp

app = Flask(__name__, template_folder='assets/templates', static_folder='assets/static')


app.register_blueprint(general_bp)