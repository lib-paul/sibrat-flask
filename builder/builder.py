from flask import Blueprint,render_template, request, redirect, url_for,session,flash

builder_bp = Blueprint('builder',__name__,template_folder="templates")

@builder_bp.route('/armador_manual')
def armador_manual_vista():
    return render_template('armador-manual.html')