from flask import Blueprint, render_template, request, redirect, url_for,session,flash
from models import *
from utils.db import db

admin_bp = Blueprint('admin',__name__,template_folder='templates')

@admin_bp.route('/abm')
def abm():
    return render_template('abm-inicio.html')
@admin_bp.route('/abm_componentes')
def abm_componentes():
    return render_template('abm-componentes.html')