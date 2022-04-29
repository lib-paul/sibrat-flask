from flask import Blueprint, render_template

general_bp = Blueprint('general',__name__, template_folder='templates')

@general_bp.route('/')
def Index():
    return render_template('general/index.html')