# app_factory.py
from flask import Flask
from api_routes import api_blueprint
from flask_cors import CORS
import boto3

def create_app(config_object='settings_module.ConfigClass'):
    app = Flask(__name__)
    app.config.from_object(config_object)
    
    dynamodb = boto3.resource('dynamodb', region_name='us-west-2')
    app.config['DYNAMODB_TABLE'] = dynamodb.Table(app.config['DYNAMODB_TABLENAME'])
    
    app.register_blueprint(api_blueprint, url_prefix='/api')
    
    
    CORS(app)
    return app
