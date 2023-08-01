from flask import Flask
from .graph.GerarGrafo import gerarGrafo


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'Sugoma'

    from .views import views
    app.register_blueprint(views, url_prefix='/')
    G = gerarGrafo()
    return app
