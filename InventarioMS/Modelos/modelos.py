from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Producto(db.Model):
    sku = db.Column(db.String, primary_key=True)
    nombre = db.Column(db.String(100))
    precio = db.Column(db.Float)
    medida = db.Column(db.Float)
    costo = db.Column(db.Float)
    ## aqui va el tipoproducto
    fechaVencimiento = db.Column(db.Date)
    descripcion = db.Column(db.String(100))
    condicionesAlmacenamiento = db.Column(db.String(100))
    fotografia = db.Column(db.String(100))
    caracteristicas = db.Column(db.String(100))

    def __repr__(self):
        return "{}-{}".format(self.sku, self.nombre)