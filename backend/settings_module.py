# settings_module.py
import os




class ConfigClass:
    DEBUG = True  # Enable or disable Flask's debug mode
    HOST = '0.0.0.0'
    PORT = 8080
    REGION = 'us-west-2'
    DYNAMODB_TABLENAME = 'piggy-finance-db'