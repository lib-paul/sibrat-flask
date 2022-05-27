from flask import Blueprint,render_template, request, redirect, url_for,session,flash
from models.Motherboard import Motherboard
from models.Cpu import Cpu
from models.Ram import Ram
from models.Gpu import Gpu
from models.Almacenamiento import Almacenamiento
from models.Fuente import Fuente
from models.Gabinete import Gabinete
from utils.db import db

builder_bp = Blueprint('builder',__name__,template_folder="templates")

@builder_bp.route('/armador_manual')
def armador_manual_vista():
    return render_template('armador-manual.html')

#Carga de items y templates para cada componente
@builder_bp.route('/agregar_componente/<id>')
def mostrar_componente(id):
    if id == '1':
        return render_template('/agregar-motherboard.html', datos=Motherboard.query.all(), id=1)
    elif id == '2':
        return render_template('/agregar-cpu.html', datos=Cpu.query.all(), id=2)
    elif id == '3':
        return render_template('/agregar-ram.html', datos=Ram.query.all(), id=3)
    elif id == '4':
        return render_template('/agregar-gpu.html', datos=Gpu.query.all(), id=4)
    elif id == '5':
        return render_template('/agregar-almacenamiento.html', datos=Almacenamiento.query.all(), id=5)
    elif id == '6':
        return render_template('/agregar-almacenamiento.html', datos=Almacenamiento.query.all(), id=6)
    elif id == '7':
        return render_template('/agregar-fuente.html', datos=Fuente.query.all(), id=7)
    elif id == '8':
        return render_template('/agregar-gabinete.html', datos=Gabinete.query.all(), id=8)
    else:    
        return render_template('armador-manual.html')

#Agregar item de 'x' componente a la vista de armador manual
@builder_bp.route('/agregar_armador/<id>/<component>', methods=['POST'])
def agregar_armador(id, component):
    if component == 'motherboard':
        data = Motherboard.query.get(id)
        session['motherboard_nombre'] = data.nombre
        session['motherboard_precio_aproximado'] = data.precio_aproximado
        session['motherboard_socket'] = data.zocalo
        session['motherboard_factor_forma'] = data.factor_forma
    elif component == 'cpu':
        data = Cpu.query.get(id)
        session['cpu_nombre'] = data.nombre
        session['cpu_precio_aproximado'] = data.precio_aproximado
    elif component == 'ram':
        data = Ram.query.get(id)
        session['ram_nombre'] = data.nombre
        session['ram_precio_aproximado'] = data.precio_aproximado
    elif component == 'gpu':
        data = Gpu.query.get(id)
        session['gpu_nombre'] = data.nombre
        session['gpu_precio_aproximado'] = data.precio_aproximado
        session['gpu_recomendacion_psu'] = data.recomendacion_fuente
    elif component == 'almacenamiento1':
        data = Almacenamiento.query.get(id)
        session['almacenamiento1_nombre'] = data.nombre
        session['almacenamiento1_precio_aproximado'] = data.precio_aproximado
    elif component == 'almacenamiento2':
        data = Almacenamiento.query.get(id)
        session['almacenamiento2_nombre'] = data.nombre
        session['almacenamiento2_precio_aproximado'] = data.precio_aproximado
    elif component == 'fuente':
        data = Fuente.query.get(id)
        session['fuente_nombre'] = data.nombre
        session['fuente_precio_aproximado'] = data.precio_aproximado
    elif component == 'gabinete':
        data = Gabinete.query.get(id)
        session['gabinete_nombre'] = data.nombre
        session['gabinete_precio_aproximado'] = data.precio_aproximado
    return redirect(url_for('builder.armador_manual_vista'))

#Borrar item seleccionado de 'x' componente de la vista de armador manual
@builder_bp.route('/borrar_componente/<id>')
def borrar_componente(id):
    if id == '1':
        session.pop('motherboard_nombre')
        session.pop('motherboard_precio_aproximado')
        session.pop('motherboard_socket')
        session.pop('motherboard_factor_forma')
    elif id == '2':
        session.pop('cpu_nombre')
        session.pop('cpu_precio_aproximado')
    elif id == '3':
        session.pop('ram_nombre')
        session.pop('ram_precio_aproximado')
    elif id == '4':
        session.pop('gpu_nombre')
        session.pop('gpu_precio_aproximado')
        session.pop('gpu_recomendacion_psu')
    elif id == '5':
        session.pop('almacenamiento1_nombre')
        session.pop('almacenamiento1_precio_aproximado')
    elif id == '6':
        session.pop('almacenamiento2_nombre')
        session.pop('almacenamiento2_precio_aproximado')
    elif id == '7':
        session.pop('fuente_nombre')
        session.pop('fuente_precio_aproximado')
    elif id == '8':
        session.pop('gabinete_nombre')
        session.pop('gabinete_precio_aproximado')
    return redirect(url_for('builder.armador_manual_vista'))