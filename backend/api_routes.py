# user_routes.py
from flask import current_app, request, Blueprint, jsonify
from time import time
import datetime

api_blueprint = Blueprint('user', __name__)


@api_blueprint.route('/get')
def get_message():
    curTime = time()
    curDateTime =  datetime.datetime.fromtimestamp(curTime).strftime('%Y-%m-%d %H:%M:%S')
    current_app.logger.info(f"At get_message request, recieved {curDateTime}")
    return f'Hello from Python Backend at {curDateTime}'


@api_blueprint.route('/post_time', methods=['POST', 'GET'])
def post_time():
    current_app.logger.debug('Request URL: %s', request.url)
    current_app.logger.debug('Request Args: %s', request.args)
    current_app.logger.debug('Full Request Args: %s', request)
    table = current_app.config['DYNAMODB_TABLE']
    id = request.args.get('ID', default=None)
    time = request.args.get('Time', default=None)
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

@api_blueprint.route('/get_time', methods=['GET'])
def get_time():
    current_app.logger.debug('Request URL: %s', request.url)
    current_app.logger.debug('Request Args: %s', request.args)
    current_app.logger.debug('Full Request Args: %s', request)
    table = current_app.config['DYNAMODB_TABLE']
    id = request.args.get('ID', default=None)
    try:
        # Getting the item from DynamoDB
        response = table.get_item(
            Key={
                'ID': int(id)  # Ensure ID is an integer
            }
        )
        item = response['Item']
        current_app.logger.debug('Response Item: %s', item)
        return jsonify({'message': 'Time retrieved successfully', 'ID': int(item['ID']), 'Time': item['Time']}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500