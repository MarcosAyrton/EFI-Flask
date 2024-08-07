from flask import Flask, render_template, redirect, request, jsonify
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

@app.route("/agregar_producto", methods=['POST', 'GET'])
def agregarProductos():
    if request.method == 'POST':
        data = request.get_json() if request.is_json else request.form
        
        equipo = data.get('nombre_equipo')
        modelo = data.get('nombre_modelo')
        marca = data.get('nombre_marca')
        fabricante = data.get('nombre_fabricante')
        color = data.get('color')
        pantalla = data.get('pantalla_tamaño')
        bateria = data.get('bateria')
        camara = data.get('camara')
        cpu = data.get('cpu')
        software = data.get('tipo_software')
        stock = data.get('stock')
        precio = data.get('precio')
        cargador = data.get('cargador')
        auriculares = data.get('auriculares')
        funda = data.get('funda')
        ubicacion = data.get('ubicacion_del_equipo')
        protector = data.get('protector')
        pais = data.get('pais_del_fabricante')
        descripcion_equipo = data.get('descripcion_del_equipo')
        cantidad = data.get('cantidad_equipo')
        provincia = data.get('provincia_prov')
        num_prov = data.get('numero_de_prov')
        nombre_proveedor = data.get('nombre_proveedor')

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

        accesorios_db = Accesorio(cargador=True if cargador == 'si' else False, auriculares=True if auriculares == 'si' else False, funda=True if funda == 'si' else False, protector_de_pantalla=True if protector == 'si' else False)
        db.session.add(accesorios_db)
        db.session.commit()

        equipo_db = Equipo(nombre=equipo, modelo=modelo_db, marca=marca_db, fabricante=fabricante_db, caracteristicas=caracteristicas_db, stock=stock_db, costo=float(precio), proveedor=proveedor_db)
        db.session.add(equipo_db)
        db.session.commit()

        if request.is_json:
            return jsonify({"message": "Producto agregado correctamente"}), 201
        else:
            return redirect('/producto')
    return render_template('agregar_producto.html')

if __name__ == "__main__":
    app.run(debug=True)
