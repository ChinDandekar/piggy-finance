# app_factory.py
from flask import Flask
from user_routes import user_blueprint

def create_app(config_object='settings_module.ConfigClass'):
    app = Flask(__name__)
    app.config.from_object(config_object)
    
    app.register_blueprint(user_blueprint, url_prefix='/api')

    return app
