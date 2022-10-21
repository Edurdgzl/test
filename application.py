"""
    Configuracion e inicializacion de la aplicacion y registro de los blueprints
    Autores: David Rodriguez Fragoso, Eduardo Rodriguez, Erick Hernandez Silva
    Creado en: 18/10/2022
    Ultimo cambio: 18/10/2022
"""
from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv

# Configuracion del backend
load_dotenv()
application = app = Flask(__name__)
cors = CORS(application)

# Ruta de testing
@application.route("/")
def hello_there():
    return "General Kenobi", 200

# Registro de blueprints
from Global.Routes.Store import GLOBAL_STORE_BLUEPRINT
application.register_blueprint(GLOBAL_STORE_BLUEPRINT, url_prefix='/store')
# Configuraciones de la app

if __name__ == "__main__":
    application.run(debug=True)

