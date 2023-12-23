# backend/api/utils/dynamodb_utils.py
import boto3
from django.conf import settings
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize DynamoDB resource
mode = os.getenv('MODE', 'production')
dynamodb_region = os.getenv('DYNAMODB_REGION', 'your-default-region')


dynamodb_region = os.getenv('DYNAMODB_REGION')

# Connect to DynamoDB (defore registering blueprints)
if mode == 'production':
    dynamodb = boto3.resource('dynamodb', region_name=dynamodb_region)

else:
    # Note that host.docker.internal only works for Docker Desktop for Mac and Windows, find another solution on Linux
    dynamodb = boto3.resource('dynamodb', region_name=dynamodb_region, endpoint_url='http://host.docker.internal:8000')

# Initialize table
dynamodb_table = dynamodb.Table(settings.DYNAMODB['TABLE_NAME'])

def get_table():
    """Returns the DynamoDB table resource."""
    return dynamodb_table
