from app import db
from sqlalchemy import Numeric, ForeignKey, Boolean
from sqlalchemy.orm import relationship

class Equipo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    modelo_id = db.Column(db.Integer, db.ForeignKey("modelo.id"), nullable=False)
    categoria_id = db.Column(db.Integer, db.ForeingKey("categoria.id"), nullable=False)
    fabricante_id = db.Column(db.Integer, db.ForeingKey("fabricante.id"), nullable=False)
    caracteristicas_id = db.Column(db.Integer, db.ForeingKey("caracteristicas.id"), nullable=False)
    marca_id = db.Column(db.Integer, db.ForeingKey("marca.id"), nullable=False)
    stock_id = db.Column(db.Integer, db.ForeingKey("stock.id"), nullable=False)
    costo = db.Column(db.Float)

    modelo = relationship('Modelo', back_populates='equipo')
    categoria = relationship('Categoria', back_pupulates='equipo')
    fabricante = relationship('Fabricante', back_pupulates='equipo')
    caracteristicas = relationship('Caracteristicas', back_pupulates='equipo')
    stock = relationship('Stock', back_pupulates='equipo')
    marca = relationship('Marca', back_populates='equipo')

    def _str_(self):
        return self.nombre
        

class Modelo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    fabricante = db.Column(db.String(50), nullable=False)
    marca_id = db.Column(db.Integer, db.ForeignKey("marca.id"), nullable=False)
    equipo_id = db.Column(db.Integer, db.ForeignKey("equipo.id"), nullable=False)
    descripcion = db.Column(db.String(100), nullable=False)

    marca = relationship('Marca', back_populates='modelo')
    equipo = relationship('Equipo', back_populates='modelo')
    
    def _str_(self):
        return self.nombre


class Marca(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    fabricante_id = db.Column(db.Integer, db.ForeingKey("fabricante.id"), nullable=False)
    
    
    fabricante = relationship('Fabricante', back_populates='marca')
    equipo = relationship('Equipo', back_populates='marca')

    def _str_(self):
        return self.nombre 

class Fabricante(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    pais_origen = db.Column(db.String(70),nullable=False)

    marca = relationship('Marca', back_populates='fabricante')
    equipo = relationship('Equipo', back_populates='fabricante')

    def _str_(self):
        return self.nombre 

class Caracteristicas(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    color = db.Column(db.String(50), nullable=False)
    pantalla = db.Column(db.String(50), nullable=False)
    bateria = db.Column(db.String(50), nullable=False)
    camara = db.Column(db.String(50), nullable=False)
    cpu  = db.Column(db.String(50), nullable=False)
    software = db.Column(db.String(50), nullable=False)

    equipo = relationship('Equipo', back_populates='caracteristicas')

    def _str_(self):
        return self.id 
    
class Stock(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cantidad = db.Column(db.Float)
    disponibilidad = db.Column(db.Boolean, default=True)
    ubicacion = db.Column(db.String(50), nullable=False)
    
    equipo = relationship('Equipo', back_populates='stock')

    def _str_(self):
        return self.cantidad

class Proveedor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    Num_telefon = db.Column(db.Float)
    provincia = db.Column(db.String(50), nullable=False)
    
    def _str_(self):
        return self.nombre

class Accesorio(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cargador = db.Column(db.Boolean, default=True)
    auriculares = db.Column(db.Boolean, default=True)
    funda = db.Column(db.Boolean, default=True)
    protector_de_pantalla = db.Column(db.Boolean, default=True)