# app_factory.py
from flask import Flask
from api_routes import api_blueprint
from flask_cors import CORS
import boto3
import os
from dotenv import load_dotenv

def create_app(config_object='settings_module.ConfigClass'):
    app = Flask(__name__)
    app.config.from_object(config_object)
    
    load_dotenv()
    mode = os.getenv('MODE', 'production')
    dynamodb_region = os.getenv('DYNAMODB_REGION', 'your-default-region')

    
    dynamodb_region = os.getenv('DYNAMODB_REGION')
    app.logger.info(f"Connecting to DynamoDB in {dynamodb_region}")
    
    # Connect to DynamoDB (defore registering blueprints)
    if mode == 'production':
        app.logger.info('Connecting to DynamoDB in production mode')
        dynamodb = boto3.resource('dynamodb', region_name=dynamodb_region)
    
    else:
        app.logger.info('Connecting to DynamoDB in development mode')
        # Note that host.docker.internal only works for Docker Desktop for Mac and Windows, find another solution on Linux
        dynamodb = boto3.resource('dynamodb', region_name=dynamodb_region, endpoint_url='http://host.docker.internal:8000')
    app.config['DYNAMODB_TABLE'] = dynamodb.Table(app.config['DYNAMODB_TABLENAME'])
    
    # Register blueprints
    app.register_blueprint(api_blueprint, url_prefix='/api')
    
    
    CORS(app)
    return app
