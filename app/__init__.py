from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options

# Initializing application
bootstrap = Bootstrap()

def create_app(config_name):

    app = Flask(__name__)

#initialize flask extensions
    bootstrap.init_app(app)
# Setting up configuration
    app.config.from_object(config_options[config_name])
# register_blueprint
    from.main import main as main_blueprint
    app.register_blueprint(main_blueprint)


    return app