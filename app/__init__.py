from flask import Flask
from .routes import main as main_blueprint

def create_app():
    app = Flask(__name__)

    # Registrar as rotas
    app.register_blueprint(main_blueprint)

    return app
