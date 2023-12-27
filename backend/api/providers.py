# api/adapters.py
from allauth.socialaccount.providers.google.provider import GoogleProvider
from django.conf import settings
from allauth.socialaccount.providers.__init__ import ProviderRegistry
import logging

logger = logging.getLogger(__name__)

class CustomGoogleProvider(GoogleProvider):
    def get_callback_url(self, request, app):
        # Use custom redirect URI for Google provider
        print(f"Provider: {app.provider}")
        if app.provider == 'google':
            logger.info(f"Google Redirect URI: {settings.GOOGLE_REDIRECT_URI}")
            return settings.GOOGLE_REDIRECT_URI
        # Fallback to default behavior for other providers
        logger.info(f"Default Redirect URI: {super().get_callback_url(request, app)}")
        return super().get_callback_url(request, app)


ProviderRegistry.register(CustomGoogleProvider)