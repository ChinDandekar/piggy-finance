from flask import Flask
from flask_cors import CORS
from time import time
import datetime

app = Flask(__name__)
CORS(app)

@app.route('/app/get')
def get_message():
    curTime = time()
    curDateTime =  datetime.datetime.fromtimestamp(curTime).strftime('%Y-%m-%d %H:%M:%S')
    return f'Hello from Python Backend at {curDateTime}'

if __name__ == '__main__':
    app.run(port=8000)
