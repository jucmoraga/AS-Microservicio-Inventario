from InventarioMS import create_app
from .Modelos import db, Producto, Bodega
from flask_restful import Api
from .Vistas import VistaProducto, VistaInventario, entradaAleatoria, salidaAleatoria
from .dataexperimento import bodegasExperimento, productosExperimento


app = create_app('default')
app_context = app.app_context()
app_context.push()

db.init_app(app)
db.create_all()

api = Api(app)
api.add_resource(VistaProducto, '/productos')
api.add_resource(VistaInventario, '/inventarios')
api.add_resource(entradaAleatoria, '/entradaAleatoria')
api.add_resource(salidaAleatoria, '/salidaAleatoria')


### Carga de datos de prueba
nBodegas = Bodega.query.count()
if(nBodegas==0):
    for bodega in bodegasExperimento.bodegas:
        db.session.add(bodega)
    db.session.commit()

nProductos = Producto.query.count()
if(nProductos==0):
    for producto in productosExperimento.productos:
        db.session.add(producto)
    db.session.commit()