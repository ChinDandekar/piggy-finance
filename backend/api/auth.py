from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from .utils.dynamodb_utils import get_table

def google_login(request):
    return JsonResponse({'message': 'Google login successful'})