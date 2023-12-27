from allauth.socialaccount.providers.oauth2.views import OAuth2View
from datetime import timedelta
from requests import RequestException

from django.core.exceptions import PermissionDenied
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone

from allauth.socialaccount.helpers import (
    complete_social_login,
    render_authentication_error,
)
from allauth.socialaccount.models import SocialLogin
from allauth.socialaccount.providers.base import ProviderException
from allauth.socialaccount.providers.base.constants import (
    AuthError,
)
from allauth.socialaccount.providers.oauth2.client import (
    OAuth2Error,
)
from allauth.utils import get_request_param

import logging

logger = logging.getLogger(__name__)

class CustomGoogleOAuth2CallbackView(OAuth2View):
    def dispatch(self, request, *args, **kwargs):
        logger.info("Entering dispatch method")
        provider = self.adapter.get_provider()
        logger.info(f"Provider: {provider}")
        if "error" in request.GET or "code" not in request.GET:
            # Distinguish cancel from error
            auth_error = request.GET.get("error", None)
            if auth_error == self.adapter.login_cancelled_error:
                error = AuthError.CANCELLED
            else:
                error = AuthError.UNKNOWN
            logger.info(f"Error: {error}")
            return render_authentication_error(
                request,
                provider,
                error=error,
                extra_context={
                    "callback_view": self,
                },
            )
        app = provider.app
        logger.info(f"App: {app}")
        client = self.get_client(self.request, app)
        logger.info(f"Client: {client}")

        try:
            access_token = self.adapter.get_access_token_data(request, app, client)
            logger.info(f"Access Token: {access_token}")
            token = self.adapter.parse_token(access_token)
            logger.info(f"Token: {token}")
            if app.pk:
                token.app = app
            login = self.adapter.complete_login(
                request, app, token, response=access_token
            )
            logger.info(f"Login: {login}")
            login.token = token
            if self.adapter.supports_state:
                login.state = SocialLogin.verify_and_unstash_state(
                    request, get_request_param(request, "state")
                )
            else:
                login.state = SocialLogin.unstash_state(request)
            logger.info("Dispatch method completed successfully")
            return complete_social_login(request, login)
        except (
            PermissionDenied,
            OAuth2Error,
            RequestException,
            ProviderException,
        ) as e:
            logger.info(f"Exception occurred: {e}")
            return render_authentication_error(request, provider, exception=e)