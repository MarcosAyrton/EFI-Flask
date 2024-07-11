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

@app.route("/producto")
def producto():
    return render_template('producto.html')

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
        proveedor = request.form['nombre_proveedor']

        fabricante_db = Fabricante(
            nombre=fabricante,
            pais_origen=pais
        )
        db.session.add(fabricante_db)
        db.session.commit()

        marca_db = Marca(
            nombre=marca,
            fabricante=fabricante_db
        )

        db.session.add(marca_db)
        db.session.commit()

        modelo_db = Modelo(
            nombre=modelo,
            fabricante=fabricante_db.nombre,
            marca=marca_db,
            descripcion=descripcion_equipo
        )
        db.session.add(modelo_db)
        db.session.commit()

        caracteristicas_db = Caracteristicas(
            color=color,
            pantalla=pantalla,
            bateria=bateria,
            camara=camara,
            cpu=cpu,
            software=software
        )
        db.session.add(caracteristicas_db)
        db.session.commit()

        stock_db = Stock(
            cantidad=1 if stock == 'si' else 0,
            disponibilidad=True if stock == 'si' else False,
            ubicacion=ubicacion
        )

        db.session.add(stock_db)
        db.session.commit()

        equipo_db = Equipo(
            nombre=equipo,
            modelo=modelo_db,
            marca=marca_db,
            fabricante=fabricante_db,
            caracteristicas=caracteristicas_db,
            stock=stock_db,
            costo=float(precio)
        )

        db.session.add(equipo_db)
        db.session.commit()

        proveedor_db = Proveedor(
            nombre=proveedor,
            num_telefono=num_prov,
            provincia=provincia
        )
        db.session.add(proveedor_db)
        db.session.commit()

        accesorios_db = Accesorio(
            cargador=True if cargador == 'si' else False,
            auriculares=True if auriculares == 'si' else False,
            funda=True if funda == 'si' else False,
            protector_de_pantalla=True if protector == 'si' else False
        )

        db.session.add(accesorios_db)
        db.session.commit()

        return redirect('/stock')  # Redirige a 'Stock' una vez guardado lo ingresado
    return render_template('agregar_producto.html')


@app.route("/stock")
def mostrarStock():
    return render_template('stock.html')
