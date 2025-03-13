from flask_restful import Resource
from ..Modelos import db, Producto, Inventario, Bodega, ProductoSchema, InventarioSchema
from flask import request
from datetime import datetime, timedelta
import random

class VistaProducto(Resource):
    def get(self):
        productos = Producto.query.all()
        return [ProductoSchema().dump(producto) for producto in productos]


class VistaInventario(Resource):
    def get(self):
        inventarios = Inventario.query.all()
        return [InventarioSchema().dump(inventario) for inventario in inventarios]

    def post(self):
        data = request.get_json()
        producto = Producto.query.get(data['sku'])
        if producto is None:
            return {'mensaje': 'Producto no encontrado'}, 400
        bodega = Bodega.query.get(data['bodega_id'])
        if bodega is None:
            return {'mensaje': 'Bodega no encontrada'}, 400
        inventario = Inventario(
            sku=producto.sku,
            cantidad=data['cantidad'],
            fechaCompra=datetime.strptime(data['fechaCompra'], "%Y-%m-%d").date(),
            fechaVencimiento=datetime.strptime(data['fechaVencimiento'], "%Y-%m-%d").date(),
            bodega_id=data['bodega_id']
        )
        db.session.add(inventario)
        db.session.commit()
        return {'mensaje': 'Inventario creado'}, 201
    
    def put(self):
        data = request.get_json()
        inventario = Inventario.query.get(data['id'])
        if inventario is None:
            return {'mensaje': 'Inventario no encontrado'}, 400
        inventario.cantidad = inventario.cantidad - data['salida']
        db.session.commit()
        return {'mensaje': 'Inventario actualizado'}, 200

class entradaAleatoria(Resource):
    def get(self):
        inventario = Inventario(
            sku=random.choice(Producto.query.all()).sku,
            cantidad=random.randint(1, 100),
            fechaCompra=datetime.now().date(),
            fechaVencimiento=(datetime.now()+timedelta(days=365)).date(),
            bodega_id=random.choice(Bodega.query.all()).id
        )
        return [InventarioSchema().dump(inventario)]

class salidaAleatoria(Resource):
    def get(self):
        inventario = random.choice(Inventario.query.all())
        cantidad = inventario.cantidad
        id = inventario.id
        cantidad = random.randint(1, cantidad)
        return {'id': id, 'salida': cantidad}