from django.db import models
from allauth.socialaccount.signals import pre_social_login
from django.dispatch import receiver
import logging

# Set up logging (configure as needed)
logger = logging.getLogger(__name__)

@receiver(pre_social_login)
def pre_social_login_debug(sender, request, sociallogin, **kwargs):
    # Log the provider and user information
    provider = sociallogin.account.provider
    user = sociallogin.user
    logger.info(f"Attempting social login - Provider: {provider}, User: {user}, Request: {request}, Sociallogin: {sociallogin}, Kwargs: {kwargs}")

    # You can also inspect the sociallogin and request objects for more details
    # Be cautious with personal information and ensure any logging is secure



# Create your models here.
