from app import db
from sqlalchemy import ForeignKey, Boolean, String, Float, Integer
from sqlalchemy.orm import relationship

class Equipo(db.Model):
    id = db.Column(Integer, primary_key=True)
    nombre = db.Column(String(50), nullable=False)
    modelo_id = db.Column(Integer, db.ForeignKey("modelo.id"), nullable=False)
    fabricante_id = db.Column(Integer, db.ForeignKey("fabricante.id"), nullable=False)
    caracteristicas_id = db.Column(Integer, db.ForeignKey("caracteristicas.id"), nullable=False)
    marca_id = db.Column(Integer, db.ForeignKey("marca.id"), nullable=False)
    stock_id = db.Column(Integer, db.ForeignKey("stock.id"), nullable=False)
    costo = db.Column(Float)
    proveedor_id = db.Column(Integer, db.ForeignKey("proveedor.id"), nullable=False)
    accesorios_id = db.Column(Integer, db.ForeignKey("accesorio.id"), nullable=False)

    modelo = relationship('Modelo', back_populates='equipos')
    fabricante = relationship('Fabricante', back_populates='equipos')
    caracteristicas = relationship('Caracteristicas', back_populates='equipos')
    stock = relationship('Stock', back_populates='equipos')
    marca = relationship('Marca', back_populates='equipos')
    proveedor = relationship('Proveedor', back_populates='equipos')
    accesorios = relationship('Accesorio', back_populates='equipos')


    def _str_(self):
        return self.nombre

class Modelo(db.Model):
    id = db.Column(Integer, primary_key=True)
    nombre = db.Column(String(100), nullable=False)
    fabricante = db.Column(String(100), nullable=False)
    marca_id = db.Column(Integer, db.ForeignKey("marca.id"), nullable=False)
    descripcion = db.Column(String(100), nullable=False)

    marca = relationship('Marca', back_populates='modelos')
    equipos = relationship('Equipo', back_populates='modelo')

    def _str_(self):
        return self.nombre

class Marca(db.Model):
    id = db.Column(Integer, primary_key=True)
    nombre = db.Column(String(50), nullable=False)
    fabricante_id = db.Column(Integer, db.ForeignKey("fabricante.id"), nullable=False)
    
    fabricante = relationship('Fabricante', back_populates='marcas')
    equipos = relationship('Equipo', back_populates='marca')
    modelos = relationship('Modelo', back_populates='marca')

    def _str_(self):
        return self.nombre 

class Fabricante(db.Model):
    id = db.Column(Integer, primary_key=True)
    nombre = db.Column(String(100), nullable=False)
    pais_origen = db.Column(String(100), nullable=False)

    marcas = relationship('Marca', back_populates='fabricante')
    equipos = relationship('Equipo', back_populates='fabricante')

    def __str__(self):
        return self.nombre 


class Caracteristicas(db.Model):
    id = db.Column(Integer, primary_key=True)
    color = db.Column(String(80), nullable=False)
    pantalla = db.Column(String(100), nullable=False)
    bateria = db.Column(String(50), nullable=False)
    camara = db.Column(String(100), nullable=False)
    cpu = db.Column(String(80), nullable=False)
    software = db.Column(String(50), nullable=False)

    equipos = relationship('Equipo', back_populates='caracteristicas')

    def _str_(self):
        return self.id 

class Stock(db.Model):
    id = db.Column(Integer, primary_key=True)
    cantidad = db.Column(Float)
    disponibilidad = db.Column(Boolean, default=True)
    ubicacion = db.Column(String(100), nullable=False)
    
    equipos = relationship('Equipo', back_populates='stock')

    def _str_(self):
        return str(self.cantidad)

class Proveedor(db.Model):
    id = db.Column(Integer, primary_key=True)
    nombre = db.Column(String(100), nullable=False)  # Asegúrate de que el campo se llame 'nombre' aquí
    num_telefono = db.Column(Float)
    provincia = db.Column(String(100), nullable=False)


    equipos = relationship('Equipo', back_populates='proveedor')
    
    def __str__(self):
        return self.nombre


class Accesorio(db.Model):
    id = db.Column(Integer, primary_key=True)
    cargador = db.Column(Boolean, default=True)
    auriculares = db.Column(Boolean, default=True)
    funda = db.Column(Boolean, default=True)
    protector_de_pantalla = db.Column(Boolean, default=True)


    equipos = relationship('Equipo', back_populates='accesorios')

    def _str_(self):
        return str(self.id)
 