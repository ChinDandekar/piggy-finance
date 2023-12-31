# backend/api/views.py
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
import datetime
import logging
from .utils.dynamodb_utils import get_table

# Set up logging (configure as needed)
logger = logging.getLogger(__name__)

def get_message(request):
    cur_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    logger.info(f"At get_message request, received {cur_time}")
    return JsonResponse({'message': f'Hello from Python Backend at {cur_time}'})

@require_http_methods(["POST", "GET"])
def post_time(request):
    # Assuming you have set up DynamoDB and have a table instance
    table = get_table()  # Retrieve your DynamoDB table instance
    id = request.GET.get('ID', default=None)
    time = request.GET.get('Time', default=None)
    try:
        response = table.put_item(
            Item={
                'ID': int(id),  # Ensure ID is an integer
                'Time': time
            }
        )
        return JsonResponse({'message': 'Time posted successfully', 'ID': id, 'Time': time})
    except Exception as e:
        logger.error(str(e))
        return JsonResponse({'error': str(e)}, status=500)

@require_http_methods(["GET"])
def get_time(request):
    table = get_table()  # Retrieve your DynamoDB table instance
    id = request.GET.get('ID', default=None)
    try:
        response = table.get_item(
            Key={
                'ID': int(id)  # Ensure ID is an integer
            }
        )
        item = response['Item']
        logger.debug(f'Response Item: {item}')
        return JsonResponse({'message': 'Time retrieved successfully', 'ID': int(item['ID']), 'Time': item['Time']})
    except Exception as e:
        logger.error(str(e))
        return JsonResponse({'error': str(e)}, status=500)
