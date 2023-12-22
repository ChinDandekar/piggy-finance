# settings_module.py

class ConfigClass:
    DEBUG = False  # Enable or disable Flask's debug mode
    HOST = '0.0.0.0'
    PORT = 8000
    REGION = 'us-west-2'
    DYNAMODB_TABLENAME = 'piggy-finance-db'