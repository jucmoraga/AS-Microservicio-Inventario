from flask_sqlalchemy import SQLAlchemy
import enum

db = SQLAlchemy()

class Producto(db.Model):
    sku = db.Column(db.String, primary_key=True)
    nombre = db.Column(db.String(100))
    precio = db.Column(db.Float)
    medida = db.Column(db.Float)
    costo = db.Column(db.Float)
    TipoProducto = db.Column(db.Enum(TipoProducto))
    fechaVencimiento = db.Column(db.Date)
    descripcion = db.Column(db.String(100))
    condicionesAlmacenamiento = db.Column(db.String(100))
    fotografia = db.Column(db.String(100))
    caracteristicas = db.Column(db.String(100))

    def __repr__(self):
        return "{}-{}".format(self.sku, self.nombre)
    
class Inventario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sku = db.Column(db.String, db.ForeignKey('producto.sku'))
    cantidad = db.Column(db.Integer)
    fechaCompra = db.Column(db.Date)
    bodega = db.Column(db.Integer, db.ForeignKey('bodega.id'))

class Bodega(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100))
    direccion = db.Column(db.String(100))
    pais = db.Column(db.String(100))
    capacidad = db.Column(db.Integer)
    
class TipoProducto(enum.Enum):
    Alimento = 1
    Licores = 2
    Aseo = 3
    Otro = 4