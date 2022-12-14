from flask import Blueprint, render_template, session, request, flash,redirect,url_for
from utils.imports_admin import Faq, Tecnico
from utils.database import cleanup, db_session as db
from flask_security import current_user, auth_required
from flask_mailman import EmailMessage
import os

general_bp = Blueprint('general',__name__, template_folder='templates')

@general_bp.route('/')
def Index():
    try:
        if session.get('armador_manual') == None:
            session['armador_manual'] = {}
        if current_user.is_authenticated:
            session['username'] = current_user.username
        else:
            if session.get('username'):
                session.pop('username')
            if session.get('armador_manual'):
                session.pop('armador_manual')   
    except Exception as e:
        db.rollback()
        raise e
    finally:
        cleanup(db)

  
    return render_template('general/index.html')


@general_bp.route('/faq')
def preguntas_frecuentes():
    try:
        faqData = Faq.query.all()
    except Exception as e:
        db.rollback()
        print(e)    
    finally:
        cleanup(db) 
    return render_template('general/faq.html', faqData = faqData)

@general_bp.route('/profile')
@auth_required()
def perfil():
    if current_user.has_role('Tecnico1') or current_user.has_role('Tecnico2'):
        tecnico = Tecnico.query.filter_by(user_id = current_user.id).one()
        return render_template('general/profile.html',tecnico=tecnico)
    else:
        return render_template('general/profile.html')
    


@general_bp.route('/solicitar_tecnico', methods=['GET','POST'])
@auth_required()
def solicitar_tecnico():

    solicitud_anterior = 1
    try:
        tecnico = Tecnico.query.filter_by(user_id = current_user.id).one()
    except Exception as e:
        solicitud_anterior = 0
    
    if solicitud_anterior == 1:
        flash("Ya has realizado la solicitud, espera la confirmacion del administrador")
        return redirect(url_for('general.perfil'))
    else:
        if request.method == 'POST':
            if request.form['titulo'] == "" or request.form['link_profesional'] == "":
                flash('¡El titulo o link profesional esta vacio!')
            else:
                link_profesional = request.form['link_profesional']
                titulo = request.form['titulo']
                descripcion_adicional = request.form['descripcion_adicional']
                try:
                    nuevo_tecnico = Tecnico(link_profesional,titulo,descripcion_adicional,current_user.id)
                    db.add(nuevo_tecnico)
                    db.commit()
                except Exception as e:
                    flash('Se encontro un error vuelva a intentar mas tarde porfavor')
                    print(e)
            return redirect(url_for('general.perfil'))
    return render_template('general/solicitud_tecnico.html')

@general_bp.route('/contacto', methods=['GET','POST'])
def contacto():
    if request.method == 'POST':
        nombre = request.form['nombre']
        mensaje = request.form['texto-largo']
        email = request.form['email']
        if nombre == "" or mensaje == "" or email == "":
            flash('Tenes campos vacios')
        else:
            receptor = os.environ.get('MAIL_USERNAME')
            msg = EmailMessage(
            'Consulta recibida SIBRAT de' + nombre,
            mensaje,
            email,
            [receptor],
            [''],
            reply_to=[email],
            headers={'Message-ID': 'foo'},
            )
            msg.send()
            flash('¡Mensaje Enviado!')
            return redirect(url_for('general.index'))
    return render_template('general/contacto.html')