# user_routes.py
from flask import current_app, request, Blueprint, jsonify
from time import time
import datetime

api_blueprint = Blueprint('user', __name__)

table = current_app.config['DYNAMODB_TABLE']

@api_blueprint.route('/get')
def get_message():
    curTime = time()
    curDateTime =  datetime.datetime.fromtimestamp(curTime).strftime('%Y-%m-%d %H:%M:%S')
    return f'Hello from Python Backend at {curDateTime}'


@api_blueprint.route('/post_time', methods=['POST'])
def post_time():
    content = request.get_json()
    id = content['ID']
    time = content.get('Time', datetime.datetime.now().isoformat()) 
    try:
        # Inserting the item into DynamoDB
        response = table.put_item(
            Item={
                'ID': int(id),  # Ensure ID is an integer
                'Time': time
            }
        )
        return jsonify({'message': 'Time posted successfully', 'ID': id, 'Time': time}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500