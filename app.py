from flask import Flask, render_template, redirect, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/Tomastemarc_Cell_DB'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from models import (
    Equipo,
    Modelo,
    Marca,
    Fabricante,
    Caracteristicas,
    Stock,
    Proveedor,
    Accesorio
)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/producto")
def producto():
    equipos = Equipo.query.all()
    return render_template('producto.html', equipos=equipos)

@app.route("/producto/<int:id>", methods=['POST', 'GET'])
def actualizar_o_eliminar_producto(id):
    equipo = Equipo.query.get_or_404(id)
    
    if request.method == 'POST':
        if 'accion' in request.form:
            if request.form['accion'] == 'actualizar':
                equipo.nombre = request.form['nombre_equipo']
                equipo.modelo.nombre = request.form['nombre_modelo']
                equipo.marca.nombre = request.form['nombre_marca']
                equipo.fabricante.nombre = request.form['nombre_fabricante']
                equipo.caracteristicas.color = request.form['color']
                equipo.caracteristicas.pantalla = request.form['pantalla_tamaño']
                equipo.caracteristicas.bateria = request.form['bateria']
                equipo.caracteristicas.camara = request.form['camara']
                equipo.caracteristicas.cpu = request.form['cpu']
                equipo.caracteristicas.software = request.form['tipo_software']
                equipo.stock.cantidad = request.form['cantidad_equipo']
                equipo.stock.disponibilidad = True if request.form.get('stock') == 'si' else False
                equipo.stock.ubicacion = request.form['ubicacion_del_equipo']
                equipo.costo = float(request.form['precio'])
                
                # Accesorio actualización
                if equipo.accesorios is None:
                    equipo.accesorios = Accesorio(
                        cargador=True if request.form.get('cargador') else False,
                        auriculares=True if request.form.get('auriculares') else False,
                        funda=True if request.form.get('funda') else False,
                        protector_de_pantalla=True if request.form.get('protector') else False
                    )
                

                # Actualizar o crear proveedor
                proveedor = Proveedor.query.filter_by(id=equipo.proveedor_id).first()
                if proveedor:
                    proveedor.nombre = request.form['nombre_proveedor']
                    proveedor.num_telefono = request.form['numero_de_prov']
                    proveedor.provincia = request.form['provincia_prov']
                else:
                    proveedor = Proveedor(
                        nombre=request.form['nombre_proveedor'],
                        num_telefono=request.form['numero_de_prov'],
                        provincia=request.form['provincia_prov']
                    )
                    db.session.add(proveedor)
                    db.session.commit()
                    equipo.proveedor_id = proveedor.id

                # Actualizar accesorios
                equipo.accesorios.cargador = True if request.form.get('cargador') else False
                equipo.accesorios.auriculares = True if request.form.get('auriculares') else False
                equipo.accesorios.funda = True if request.form.get('funda') else False
                equipo.accesorios.protector_de_pantalla = True if request.form.get('protector') else False

                db.session.commit()
                return redirect('/producto')
            
            elif request.form['accion'] == 'eliminar':
                db.session.delete(equipo)
                db.session.commit()
            return redirect('/producto')
    
    return render_template('producto_editar.html', equipo=equipo)

@app.route("/agregar_producto", methods=['POST', 'GET'])
def agregarProductos():
    if request.method == 'POST':
        equipo = request.form['nombre_equipo']
        modelo = request.form['nombre_modelo']
        marca = request.form['nombre_marca']
        fabricante = request.form['nombre_fabricante']
        color = request.form['color']
        pantalla = request.form['pantalla_tamaño']
        bateria = request.form['bateria']
        camara = request.form['camara']
        cpu = request.form['cpu']
        software = request.form['tipo_software']
        stock = request.form['stock']
        precio = request.form['precio']
        cargador = request.form['cargador']
        auriculares = request.form['auriculares']
        funda = request.form['funda']
        ubicacion = request.form['ubicacion_del_equipo']
        protector = request.form['protector']
        pais = request.form['pais_del_fabricante']
        descripcion_equipo = request.form['descripcion_del_equipo']
        cantidad = request.form['cantidad_equipo']
        provincia = request.form['provincia_prov']
        num_prov = request.form['numero_de_prov']
        nombre_proveedor = request.form['nombre_proveedor']

        # Buscar o crear las instancias de los modelos relacionados
        fabricante_db = Fabricante.query.filter_by(nombre=fabricante).first()
        if not fabricante_db:
            fabricante_db = Fabricante(nombre=fabricante, pais_origen=pais)
            db.session.add(fabricante_db)
            db.session.commit()

        marca_db = Marca.query.filter_by(nombre=marca).first()
        if not marca_db:
            marca_db = Marca(nombre=marca, fabricante=fabricante_db)
            db.session.add(marca_db)
            db.session.commit()

        modelo_db = Modelo.query.filter_by(nombre=modelo).first()
        if not modelo_db:
            modelo_db = Modelo(nombre=modelo, fabricante=fabricante_db.nombre, marca=marca_db, descripcion=descripcion_equipo)
            db.session.add(modelo_db)
            db.session.commit()

        caracteristicas_db = Caracteristicas(color=color, pantalla=pantalla, bateria=bateria, camara=camara, cpu=cpu, software=software)
        db.session.add(caracteristicas_db)
        db.session.commit()

        stock_db = Stock(cantidad=cantidad, disponibilidad=True if stock == 'si' else False, ubicacion=ubicacion)
        db.session.add(stock_db)
        db.session.commit()

        proveedor_db = Proveedor.query.filter_by(nombre=nombre_proveedor).first()
        if not proveedor_db:
            proveedor_db = Proveedor(nombre=nombre_proveedor, num_telefono=num_prov, provincia=provincia)
            db.session.add(proveedor_db)
            db.session.commit()

        accesorios_db = Accesorio(cargador=True if cargador == 'si' else False, 
        auriculares=True if auriculares == 'si' else False, 
        funda=True if funda == 'si' else False, 
        protector_de_pantalla=True if protector == 'si' else False
        )
        
        db.session.add(accesorios_db)
        db.session.commit()

        equipo_db = Equipo(nombre=equipo, modelo=modelo_db, marca=marca_db, 
        fabricante=fabricante_db, 
        caracteristicas=caracteristicas_db, 
        stock=stock_db, costo=float(precio), 
        proveedor=proveedor_db,
        accesorios=accesorios_db
        )
        
        db.session.add(equipo_db)
        db.session.commit()
        

        return redirect('/producto')
    return render_template('agregar_producto.html')

