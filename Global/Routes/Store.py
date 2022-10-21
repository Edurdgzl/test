"""

"""

from urllib import request
from flask import Blueprint
from Global.Controllers import Store as c

GLOBAL_STORE_BLUEPRINT = Blueprint('GLOBAL_STORE_BLUEPRINT', __name__)

@GLOBAL_STORE_BLUEPRINT.route('/create', methods = ['POST'])
def createStore():
    return c.create_store()

@GLOBAL_STORE_BLUEPRINT.route('/getProducts', methods = ['GET'])
def getStoreProducts():
    return c.get_store_products()
"""
estadisticas para todos
- los mas comprandos
- los menos comprados

estadísticas por tienda
- los productos


estadisticas gobales, estado
la tiendita que mas compra
la tiendita que menos compra

-------------------

Ruta que devuelva todas las tienditas 
- toda la informacion

Ruta que devuelve los pedidos ordenados en orden descendente para 

Ruta para crear pedido 

IMPORTANTE

RUTA PARA ESTADISTICAS DE LA TIENDA
- los productos de la tienda separados en agotados, existentes
- los productos 3 productos mas comprados en un intervalo de fechas 
- grafica de linea con el historico de compras con intervalos de temporalidad de 1 mes


BASE DEDATOS
QUITAR CANTIDAD
"""