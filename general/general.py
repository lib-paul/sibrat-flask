from flask import Blueprint, render_template
from utils.imports_admin import Faq

general_bp = Blueprint('general',__name__, template_folder='templates')

@general_bp.route('/')
def Index():
    return render_template('general/index.html')

@general_bp.route('/faq')
def preguntas_frecuentes():
    faqData = Faq.query.all()
    return render_template('general/faq.html', faqData = faqData)

@general_bp.route('/profile')
def prefil():
    return render_template('general/profile.html')