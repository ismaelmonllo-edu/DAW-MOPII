"""
Punto de entrada principal del servidor Flask.
Registra los Blueprints (controladores) y arranca la aplicación.
"""

from flask import Flask
from flask_cors import CORS

# Import del blueprint
from controllers.producto_controller import producto_blueprint

app = Flask(__name__)

# Habilitar CORS
CORS(app)

# Registrar blueprint
app.register_blueprint(producto_blueprint, url_prefix="/api")
#app.register_blueprint(controllers.usuario_controllers, GET api/usuarios) #cogeriamos usuarios deinidos en la BD

# Esto deberia ser in test para comprobar las rutas existentes
# with app.test_request_context():
#     print (app.url_map)

@app.route("/")
def home():
    return "Backend Flask funcionando correctamente."

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)