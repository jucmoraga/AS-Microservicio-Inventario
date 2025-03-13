from flask_sqlalchemy import SQLAlchemy
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow import fields
import enum

db = SQLAlchemy()

class TipoProducto(enum.Enum):
    Alimento = 1
    Licores = 2
    Aseo = 3
    Otro = 4

class Producto(db.Model):
    sku = db.Column(db.String, primary_key=True)
    nombre = db.Column(db.String(100))
    precio = db.Column(db.Float)
    medida = db.Column(db.Float)
    costo = db.Column(db.Float)
    Tipo = db.Column(db.Enum(TipoProducto))
    descripcion = db.Column(db.String(100))
    condicionesAlmacenamiento = db.Column(db.String(100))
    fotografia = db.Column(db.String(100))
    caracteristicas = db.Column(db.String(100))
    
class Inventario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sku = db.Column(db.String, db.ForeignKey('producto.sku'))
    producto = db.relationship('Producto', backref='inventarios')
    cantidad = db.Column(db.Integer)
    fechaCompra = db.Column(db.Date)
    fechaVencimiento = db.Column(db.Date)
    bodega_id = db.Column(db.Integer, db.ForeignKey('bodega.id'))
    bodega = db.relationship('Bodega', backref='inventarios')

class Bodega(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100))
    direccion = db.Column(db.String(100))
    pais = db.Column(db.String(100))
    capacidad = db.Column(db.Integer)
    
class EnumADiccionario(fields.Field):
    def _serialize(self, value, attr, obj, **kwargs):
        if value is None:
            return None
        return {'tipo': value.name}

class ProductoSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Producto
        include_relationships = True
        load_instance = True
    Tipo = EnumADiccionario(attribute="Tipo")

class BodegaSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Bodega
        include_relationships = True
        load_instance = True

class InventarioSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Inventario
        include_relationships = True
        load_instance = True
        id = fields.Int()
    sku = fields.Str()
    cantidad = fields.Int()
    fechaCompra = fields.Date()
    fechaVencimiento = fields.Date()
    bodega_id = fields.Int()
    producto = fields.Nested(ProductoSchema)
    bodega = fields.Nested(BodegaSchema)
