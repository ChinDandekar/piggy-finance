# api/adapters.py
from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from django.conf import settings
import logging

logger = logging.getLogger(__name__)

class CustomSocialAccountAdapter(DefaultSocialAccountAdapter):
    def get_callback_url(self, request, app):
        # Use custom redirect URI for Google provider
        if app.provider == 'google':
            return settings.GOOGLE_REDIRECT_URI
        # Fallback to default behavior for other providers
        return super().get_callback_url(request, app)