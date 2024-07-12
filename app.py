from flask import Flask, render_template, redirect, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/Tomastemarc_Cell_DB'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Agregar el from models import
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


@app.route("/agregar_producto")
def prendas():
    return render_template('agregar_producto.html')



@app.route("/agregar_producto", methods=['POST', 'GET'])
def agregarProductos():
    if request.method == 'POST':
        equipo = request.form['nombre_equipo']
        modelo_nombre = request.form['nombre_modelo']
        marca_nombre = request.form['nombre_marca']
        fabricante_nombre = request.form['nombre_fabricante']
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
        proveedor_nombre = request.form['nombre_proveedor']

        try:

            fabricante_db = Fabricante(nombre=fabricante_nombre, pais_origen=pais)
            db.session.add(fabricante_db)
            db.session.flush()  

            marca_db = Marca(nombre=marca_nombre, fabricante=fabricante_db)
            db.session.add(marca_db)
            db.session.flush()  

            modelo_db = Modelo(nombre=modelo_nombre, fabricante=fabricante_db, marca=marca_db, descripcion=descripcion_equipo)
            db.session.add(modelo_db)
            db.session.flush() 

            caracteristicas_db = Caracteristicas(color=color, pantalla=pantalla, bateria=bateria, camara=camara, cpu=cpu, software=software)
            db.session.add(caracteristicas_db)
            db.session.flush()  

            stock_db = Stock(cantidad=1 if stock == 'si' else 0, disponibilidad=True if stock == 'si' else False, ubicacion=ubicacion)
            db.session.add(stock_db)
            db.session.flush()  

            proveedor_db = Proveedor(nombre=proveedor_nombre, num_telefono=num_prov, provincia=provincia)
            db.session.add(proveedor_db)
            db.session.flush() 

            accesorios_db = Accesorio(cargador=True if cargador == 'si' else False, auriculares=True if auriculares == 'si' else False, funda=True if funda == 'si' else False, protector_de_pantalla=True if protector == 'si' else False)
            db.session.add(accesorios_db)
            db.session.flush()  

            equipo_db = Equipo(nombre=equipo, modelo=modelo_db, marca=marca_db, fabricante=fabricante_db, caracteristicas=caracteristicas_db, stock=stock_db, costo=float(precio), proveedor=proveedor_db, accesorios=accesorios_db)
            db.session.add(equipo_db)

            db.session.commit()

            productos = Equipo.query.all()
            return render_template('stock.html', productos=productos)
        except Exception as e:
            db.session.rollback()
            return f"Error: {str(e)}"
    
    return render_template('agregar_producto.html')

@app.route('/productos')
def mostrarProductos():
    productos = Equipo.query.options(
        db.joinedload(Equipo.modelo),
        db.joinedload(Equipo.marca),
        db.joinedload(Equipo.fabricante),
        db.joinedload(Equipo.caracteristicas),
        db.joinedload(Equipo.stock),
        db.joinedload(Equipo.proveedor),
        db.joinedload(Equipo.accesorios)
    ).all()

    return render_template('producto.html', productos=productos)


@app.route("/stock")
def mostrarStock():
    productos = Equipo.query.options(
        db.joinedload(Equipo.modelo),
        db.joinedload(Equipo.marca),
        db.joinedload(Equipo.fabricante),
        db.joinedload(Equipo.caracteristicas),
        db.joinedload(Equipo.stock),
        db.joinedload(Equipo.proveedor),
        db.joinedload(Equipo.accesorios)
    ).all()

    return render_template('stock.html', productos=productos)


