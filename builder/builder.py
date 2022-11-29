from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from utils.imports_admin import *


builder_bp = Blueprint('builder', __name__, template_folder="templates")


componentes = {
    "1": "Motherboard",
    "2": "CPU",
    "3": "RAM",
    "4": "GPU",
    "5": "Almacenamiento Principal",
    "6": "Almacenamiento Secundario",
    "7": "Fuente",
    "8": "Gabinete",
}

# RUTA PRINCIPAL DEL ARMADOR MANUAL


@builder_bp.route('/armador_manual')
def armador_manual_vista():

    #Calculadora de Precios :)
    precio_total = 0
    if 'armador_manual' in session and session['armador_manual'] != {} :
        print(session['armador_manual'])
        for precios in session['armador_manual'].values():
            if  precios is not None and precios.get('precio_aproximado') :
                precio_total = precios['precio_aproximado'] + precio_total
    session['precio_total_armado'] = precio_total
    
    return render_template('armador-manual.html', componentes=componentes, precio_total = precio_total, len=len)

# RUTA PARA LA CARGA DE COMPONENTES EN EL AGREGADO


@builder_bp.route('/agregar_componente/<id>')
def mostrar_componente(id):
    vista_agregar = '/agregar-componente.html'
    if id == '1':
        datos = Motherboard.query.all()
        caracteristicas_dato = Motherboard.caracteristicas_motherboard()
        componente = "motherboard"
        tipo = "motherboard"
        datos_columna = Motherboard.columnas_motherboard()
    elif id == '2':
        datos = Cpu.query.all()
        caracteristicas_dato = Cpu.caracteristicas_cpu()
        componente = "cpu"
        tipo = "cpu"
        datos_columna = Cpu.columnas_cpu()
    elif id == '3':
        datos = Ram.query.all()
        caracteristicas_dato = Ram.caracteristicas_ram()
        componente = "ram"
        tipo = "ram"
        datos_columna = Ram.columnas_ram()
    elif id == '4':
        datos = Gpu.query.all()
        caracteristicas_dato = Gpu.caracteristicas_gpu()
        componente = "gpu"
        tipo = "gpu"
        datos_columna = Gpu.columnas_gpu()
    elif id == '5':
        datos = Almacenamiento.query.all()
        caracteristicas_dato = Almacenamiento.caracteristicas_almacenamiento()
        componente = "almacenamiento"
        tipo = "almacenamiento"
        datos_columna = Almacenamiento.columnas_almacenamiento()
    elif id == '6':
        datos = Almacenamiento.query.all()
        caracteristicas_dato = Almacenamiento.caracteristicas_almacenamiento()
        componente = "almacenamiento2"
        tipo = "almacenamiento2"
        datos_columna = Almacenamiento.columnas_almacenamiento()
    elif id == '7':
        datos = Fuente.query.all()
        caracteristicas_dato = Fuente.caracteristicas_fuente()
        componente = "fuente"
        tipo = "fuente"
        datos_columna = Fuente.columnas_fuente()
    elif id == '8':
        datos = Gabinete.query.all()
        caracteristicas_dato = Gabinete.caracteristicas_gabinete()
        componente = "gabinete"
        tipo = "gabinete"
        datos_columna = Gabinete.columnas_gabinete()
    else:
        return render_template('armador-manual.html')
    
    return render_template(vista_agregar, datos=datos, id=id, caracteristicas_dato=caracteristicas_dato, componente=componente, tipo=tipo, datos_columna=datos_columna, getattr=getattr, zip=zip)

# Agregar item de 'x' componente a la vista de armador manual


@builder_bp.route('/agregar_armador/<id>/<component>', methods=['POST'])
def agregar_armador(id, component):
    if component == 'motherboard':
        data = Motherboard.query.get(id)
        session['armador_manual'].update({
            "Motherboard": {
                "marca": data.fabricante,
                "nombre": data.nombre,
                "precio_aproximado": data.precio_aproximado,
                "socket": data.zocalo,
                "factor_forma": data.factor_forma
            }
        })
    elif component == 'cpu':
        data = Cpu.query.get(id)
        session['armador_manual'].update({
            "CPU": {
                "marca": data.fabricante,
                "nombre": data.nombre,
                "precio_aproximado": data.precio_aproximado
            }
        })
    elif component == 'ram':
        data = Ram.query.get(id)
        session['armador_manual'].update({
            "RAM": {
                "marca": data.fabricante,
                "nombre": data.nombre,
                "precio_aproximado": data.precio_aproximado,
                "capacidad": data.capacidad,
                "cant_ram" : 1
            }
        })
    elif component == 'gpu':
        data = Gpu.query.get(id)
        session['armador_manual'].update({
            "GPU": {
                "marca": data.fabricante,
                "nombre": data.nombre,
                "precio_aproximado": data.precio_aproximado,
                "recomendacion_psu": data.recomendacion_fuente
            }
        })
    elif component == 'almacenamiento':
        data = Almacenamiento.query.get(id)
        session['armador_manual'].update({
            "Almacenamiento Principal": {
                "marca": data.fabricante,
                "nombre": data.nombre,
                "precio_aproximado": data.precio_aproximado,
                "capacidad" : data.capacidad
            }
        })
    elif component == 'almacenamiento2':
        data = Almacenamiento.query.get(id)
        session['armador_manual'].update({
            "Almacenamiento Secundario": {
                "marca": data.fabricante,
                "nombre": data.nombre,
                "precio_aproximado": data.precio_aproximado,
                "capacidad" : data.capacidad
            }
        })

    elif component == 'fuente':
        data = Fuente.query.get(id)
        session['armador_manual'].update({
            "Fuente": {
                "marca": data.fabricante,
                "nombre": data.nombre,
                "precio_aproximado": data.precio_aproximado
            }
        })

    elif component == 'gabinete':
        data = Gabinete.query.get(id)
        session['armador_manual'].update({
            "Gabinete": {
                "marca": data.fabricante,
                "nombre": data.nombre,
                "precio_aproximado": data.precio_aproximado
            }
        })

    return redirect(url_for('builder.armador_manual_vista'))

# Borrar item seleccionado de 'x' componente de la vista de armador manual


@builder_bp.route('/borrar_componente/<id>')
def borrar_componente(id):
    if id == '1':
        session['armador_manual'].pop('Motherboard', None)
    elif id == '2':
        session['armador_manual'].pop('CPU', None)
    elif id == '3':
        session['armador_manual'].pop('RAM', None)
    elif id == '4':
        session['armador_manual'].pop('GPU', None)
    elif id == '5':
        session['armador_manual'].pop('Almacenamiento Principal', None)
    elif id == '6':
        session['armador_manual'].pop('Almacenamiento Secundario', None)
    elif id == '7':
        session['armador_manual'].pop('Fuente', None)
    elif id == '8':
        session['armador_manual'].pop('Gabinete', None)
    return redirect(url_for('builder.armador_manual_vista'))


@builder_bp.route('/reset_armador')
def reiniciar_armador():
    session['armador_manual'].clear()
    return redirect(url_for('builder.armador_manual_vista'))


@builder_bp.route('/buscar_armados')
def buscar_armados():
    data_armados = Armados.query.all()
    return render_template('buscar-armados.html',datos = data_armados)

@builder_bp.route('/guardar_armado')
def guardar_armado():
    nombres = []
    cant_ram= session['armador_manual']['RAM']['cant_ram']
    precio_total = session['precio_total_armado']
    id_usuario = User.query.filter(User.nombre_cuenta == session['username'])
    if 'armador_manual' in session:
        for nombre in session['armador_manual'].values():
            nombres.append(nombre['marca'] + " " + nombre['nombre'])
    print(nombres)
    nuevo_armado = Armados(nombres[0],nombres[1],nombres[2],cant_ram,nombres[3],nombres[4],nombres[5],nombres[6],precio_total,1)
    db.session.add(nuevo_armado)
    db.session.commit()
    db.session.close()
    reiniciar_armador()
    flash('Armado ¡GUARDADO CORRECTAMENTE!')
    return redirect(url_for('builder.armador_manual_vista'))


@builder_bp.route('/agregar_ram/')
def agregar_ram():
    if 'armador_manual' in session:
        if 'RAM' in session['armador_manual']:
            if session['armador_manual']['RAM']['cant_ram'] < 4:
                session['armador_manual']['RAM']['cant_ram'] += 1
            else:
                flash('Maxima cantidad de RAM alcanzada')
    return redirect(url_for('builder.armador_manual_vista'))

@builder_bp.route('/eliminar_ram/')
def eliminar_ram():
    if 'armador_manual' in session:
        if 'RAM' in session['armador_manual']:
            if session['armador_manual']['RAM']['cant_ram'] > 1:
                session['armador_manual']['RAM']['cant_ram'] -= 1
            else:
                flash('Minima cantidad de RAM alcanzada')
    return redirect(url_for('builder.armador_manual_vista'))

