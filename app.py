from flask import Flask, render_template, redirect, request, jsonify, session
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
    Accesorio,
    Usuario
)

@app.route("/", methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        action = request.form.get('action')
        
        if action == 'register':
            username = request.form['username']
            password = request.form['password']
            email = request.form['email']
            
            existing_user = Usuario.query.filter_by(usuario=username).first()
            if existing_user:
                return render_template('login.html', message="El usuario ya está registrado.")
            
            new_user = Usuario(usuario=username, contraseña=password, email=email)
            db.session.add(new_user)
            db.session.commit()
            
            return redirect('/inicio_comprador')
        
        elif action == 'login':
            username = request.form['username-sign-in']
            print(username)
            password = request.form['password-sign-in']
            print(password)
            user = Usuario.query.filter_by(usuario=username, contraseña=password).first()
            if user:
                session['username-sign-in'] = username  # Guardar el nombre de usuario en la sesión
                return jsonify(success=True)
            else:
                return jsonify(success=False, message="Nombre de usuario o contraseña incorrectos.")
    
    return render_template('login.html')

@app.route("/inicio_comprador")
def home():
    return render_template('inicio-comprador.html')

@app.route("/inicio")
def homeAdmin():
    username = session.get('username')  # Recuperar el nombre de usuario de la sesión
    return render_template('index.html', username=username)

@app.route("/producto")
def producto():
    equipos = Equipo.query.all()
    return render_template('producto.html', equipos=equipos)

@app.route("/agregar_producto", methods=['POST', 'GET'])
def agregarProductos():
    if request.method == 'POST':
        # Los datos del formulario
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

        accesorios_db = Accesorio(cargador=True if cargador == 'si' else False, auriculares=True if auriculares == 'si' else False, funda=True if funda == 'si' else False, protector_de_pantalla=True if protector == 'si' else False)
        db.session.add(accesorios_db)
        db.session.commit()

        equipo_db = Equipo(nombre=equipo, modelo=modelo_db, marca=marca_db, fabricante=fabricante_db, caracteristicas=caracteristicas_db, stock=stock_db, costo=float(precio), proveedor=proveedor_db)
        db.session.add(equipo_db)
        db.session.commit()

        return redirect('/producto')
    return render_template('agregar_producto.html')

if __name__ == "__main__":
    app.run(debug=True)
