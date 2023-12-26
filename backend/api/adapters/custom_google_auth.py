from allauth.account.adapter import DefaultAccountAdapter
import logging
import os
from dotenv import load_dotenv

logger = logging.getLogger(__name__)

class CustomGoogleAccountAdapter(DefaultAccountAdapter):

    def get_login_redirect_url(self, request):
        load_dotenv('../../.env')
        logger.info("Getting login redirect URL")
        # Set URL to be google redirect URI
        url = os.getenv('GOOGLE_REDIRECT_URI')
        # Log the URL
        logger.info(f"Login Redirect URL: {url}")
        
        # Return the URL
        return url