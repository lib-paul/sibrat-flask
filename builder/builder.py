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
    print(session['armador_manual'])
    return render_template('armador-manual.html', componentes=componentes)

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
        session['armador_manual'].update( {
            "Motherboard" : {
                "marca" : data.fabricante,
                "nombre": data.nombre,
                "precio_aproximado" : data.precio_aproximado,
                "socket" : data.zocalo,
                "factor_forma" : data.factor_forma
            },
            "precios" :{
                "precio_motherboard" : data.precio_aproximado,
            },
        })
    elif component == 'cpu':
        data = Cpu.query.get(id)
        session['armador_manual'].update( {
            "CPU" : {
                "marca" : data.fabricante,
                "nombre" : data.nombre,
                "precio_aproximado" : data.precio_aproximado
            },
            "precios" :{
                "precio_cpu" : data.precio_aproximado,
            },
        })   
    elif component == 'ram':
        data = Ram.query.get(id)
        session['armador_manual'].update( {
            "RAM" : {
                "marca" : data.fabricante,
                "nombre" : data.nombre,
                "precio_aproximado" : data.precio_aproximado
            },
            "precios" :{
                "precio_ram" : data.precio_aproximado,
            },
        })   
    elif component == 'gpu':
        data = Gpu.query.get(id)
        session['armador_manual'].update( {
            "GPU" : {
                "marca" : data.fabricante,
                "nombre" : data.nombre,
                "precio_aproximado" : data.precio_aproximado,
                "recomendacion_psu" : data.recomendacion_fuente
            },
            "precios" :{
                "precio_gpu" : data.precio_aproximado,
            },
        })   
    elif component == 'almacenamiento':
        data = Almacenamiento.query.get(id)
        session['armador_manual'].update( {
            "Almacenamiento Principal" : {
                "marca" : data.fabricante,
                "nombre" : data.nombre,
                "precio_aproximado" : data.precio_aproximado
            },
            "precios" :{
                "precio_almacenamiento1" : data.precio_aproximado,
            },
        })   
        print("llegue aca")
        print(session['armador_manual'].get('Almacenamiento Principal'))
    elif component == 'almacenamiento2':
        data = Almacenamiento.query.get(id)
        session['armador_manual'].update( {
            "Almacenamiento Secundario" : {
                "marca" : data.fabricante,
                "nombre" : data.nombre,
                "precio_aproximado" : data.precio_aproximado
            },
            "precios" :{
                "precio_almacenamiento2" : data.precio_aproximado,
            },
        })   

    elif component == 'fuente':
        data = Fuente.query.get(id)
        session['armador_manual'].update( {
            "Fuente" : {
                "marca" : data.fabricante,
                "nombre" : data.nombre,
                "precio_aproximado" : data.precio_aproximado
            },
            "precios" :{
                "precio_fuente" : data.precio_aproximado,
            },
        })   

    elif component == 'gabinete':
        data = Gabinete.query.get(id)
        session['armador_manual'].update( {
            "Gabinete" : {
                "marca" : data.fabricante,
                "nombre" : data.nombre,
                "precio_aproximado" : data.precio_aproximado
            },
            "precios" :{
                "precio_gabinete" : data.precio_aproximado,
            },
        })  

    return redirect(url_for('builder.armador_manual_vista'))

# Borrar item seleccionado de 'x' componente de la vista de armador manual


@builder_bp.route('/borrar_componente/<id>')
def borrar_componente(id):
    if id == '1':
        session['armador_manual'].pop('Motherboard',None)
    elif id == '2':
        session['armador_manual'].pop('CPU',None)
    elif id == '3':
        session['armador_manual'].pop('RAM',None)
    elif id == '4':
        session['armador_manual'].pop('GPU',None)
    elif id == '5':
        session['armador_manual'].pop('Almacenamiento Principal',None)
    elif id == '6':
        session['armador_manual'].pop('Almacenamiento Secundario',None)
    elif id == '7':
        session['armador_manual'].pop('Fuente',None)
    elif id == '8':
        session['armador_manual'].pop('Gabinete',None)
    return redirect(url_for('builder.armador_manual_vista'))

@builder_bp.route('/reset_armador')
def reiniciar_armador():
    session['armador_manual'].clear()
    return redirect(url_for('builder.armador_manual_vista'))


@builder_bp.route('/buscar_armados')
def buscar_armados():
    return render_template('buscar-armados.html')