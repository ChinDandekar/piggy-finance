# backend/api/views.py
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
import datetime
import logging
from .utils.dynamodb_utils import get_table
from .utils.modify_redirect_uri import modify_redirect_uri
from django.shortcuts import redirect
from allauth.socialaccount.providers.google.views import oauth2_login
from .custom_views.CustomGoogleOauth2CallbackView import CustomGoogleOAuth2CallbackView
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter

# Set up logging (configure as needed)
logger = logging.getLogger(__name__)

def get_message(request):
    cur_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    logger.info(f"At get_message request, received {cur_time}")
    if request.user.is_authenticated:
        # User is authenticated
        full_name = request.user.get_full_name()
        user_name = full_name if full_name else request.user.username

        # User is authenticated, return a welcome message
        return JsonResponse({'message': f'Welcome: {user_name}'})
    else:
        # User is not authenticated
        return JsonResponse({'message': 'Please sign in to continue'})
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
        

def custom_google_login(request):
    # Your custom logic here
    logger.info("Custom Google login view called")
    
    oauth2_loginresponse = oauth2_login(request)
    oauth2_loginresponse['Location'] = modify_redirect_uri(oauth2_loginresponse.url)
    
    logger.info(oauth2_loginresponse)

    # Proceed with the standard oauth2_login view from django-allauth
    return oauth2_loginresponse


def custom_google_callback(request):
    # Your custom logic here
    logger.info("Custom Google callback view called")
    
    ouath2_callback = CustomGoogleOAuth2CallbackView.adapter_view(GoogleOAuth2Adapter)
    oauth2_callbackresponse = ouath2_callback(request)
    logger.info(f'Here is the callback response: {oauth2_callbackresponse}')

    # Proceed with the standard oauth2_callback view from django-allauth
    return oauth2_callbackresponse