from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
import logging
import pdb

logger = logging.getLogger(__name__)

class SocialAccountAdapter(DefaultSocialAccountAdapter):
    def authentication_error(self, request, provider_id, error, exception, extra_context):
        pdb.set_trace()
        logger.error(
            f'SocialAccount authentication error:\n request: {request},\n provider: {provider_id},\n error: {error},\n exception: {exception},\n extra_context: {extra_context}'
        )
        return super().authentication_error(request, provider_id, error, exception, extra_context)