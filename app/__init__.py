from flask import Flask
from flask_bootstrap import Bootstrap

from config import Config
from app.ibge.views import bp_ibge


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    Bootstrap(app)

    app.register_blueprint(bp_ibge)

    return app
