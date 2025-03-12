from InventarioMS import create_app
from .Modelos import db, Producto


app = create_app('default')
app_context = app.app_context()
app_context.push()

db.init_app(app)
db.create_all()
