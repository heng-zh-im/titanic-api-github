from flask import Flask
from .config import app_config
from .models import db
from .views.passenger import passenger_api as passengers

def create_app(env_name):

    # app initiliazation
    app = Flask(__name__)
    app.config.from_object(app_config[env_name])
    db.init_app(app)

    app.register_blueprint(passengers, url_prefix='/api/v1/')

    # root endpoint of the flask stillthere-api
    @app.route('/', methods=['GET'])
    def index():
        return 'Titanic passengers log'

    return app
