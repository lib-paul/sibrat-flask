from flask import Blueprint, render_template, session
from utils.imports_admin import Faq
from flask_security import current_user

general_bp = Blueprint('general',__name__, template_folder='templates')

@general_bp.route('/')
def Index():

    if session.get('armador_manual') == None:
        print('llegue')
        session['armador_manual'] = {}

    if current_user.is_authenticated:
        session['username'] = current_user.username
    else:
        if session.get('username'):
            session.pop('username')
    return render_template('general/index.html')

@general_bp.route('/faq')
def preguntas_frecuentes():
    faqData = Faq.query.all()
    return render_template('general/faq.html', faqData = faqData)

@general_bp.route('/profile')
def prefil():
    return render_template('general/profile.html')