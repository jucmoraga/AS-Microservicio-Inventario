from .Modelos import Producto, Bodega, TipoProducto
from typing import List


class bodegasExperimento:
    bodegas: List[Bodega]=[
        Bodega(id=1, nombre="Bodega Bogotá", direccion="Calle 100", pais="Colombia", capacidad=1000),
        Bodega(id=2, nombre="Bodega Barranquilla", direccion="Calle 80", pais="Colombia", capacidad=500),
        Bodega(id=3, nombre="Bodega Quito", direccion="Calle 70", pais="Ecuador", capacidad=800)
    ]

class productosExperimento:
    productos: List[Producto]=[
        Producto(sku="001", nombre="Pastas Doria", precio=5000, medida=14, costo=4000, Tipo=TipoProducto.Alimento ,descripcion="Fideo tradicional", condicionesAlmacenamiento="Seco sin refrigerar", fotografia="pasta.jpg", caracteristicas="250 gramos de pasta tipo fideo en bolsa"),
        Producto(sku="002", nombre="Aguardiente Antioqueño", precio=50000, medida=20, costo=35000, Tipo=TipoProducto.Licores , descripcion="Botella de litro", condicionesAlmacenamiento="Sin refrigerar", fotografia="guaro.jpg", caracteristicas="Botella de litro tapa azul"),
        Producto(sku="003", nombre="Jabón Rey", precio=4000, medida=12, costo=3400, Tipo=TipoProducto.Aseo , descripcion="Barra de jabón azul", condicionesAlmacenamiento="Seco y frio", fotografia="jabon.jpg", caracteristicas="Barra color azul de 100 gramos"),
        Producto(sku="004", nombre="Kilométrico", precio=2000, medida=12, costo=1000, Tipo=TipoProducto.Otro , descripcion="Esfero de tinta negra", condicionesAlmacenamiento="Seco", fotografia="kilometrico.jpg", caracteristicas="Esfero de tinta negra con tapa")  
    ]
