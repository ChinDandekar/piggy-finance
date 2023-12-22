# user_routes.py
from flask import Blueprint
from time import time
import datetime

api_blueprint = Blueprint('user', __name__)

@api_blueprint.route('/get')
def get_message():
    curTime = time()
    curDateTime =  datetime.datetime.fromtimestamp(curTime).strftime('%Y-%m-%d %H:%M:%S')
    return f'Hello from Python Backend at {curDateTime}'
