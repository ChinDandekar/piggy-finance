import logging

class SocialAuthDebugMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.logger = logging.getLogger(__name__)

    def __call__(self, request):
        response = self.get_response(request)
        # if request.path.startswith('/api/google/login/callback/'):
        #     self.log_failure_details(request)
        return response

    def process_exception(self, request, exception):
        if request.path.startswith('/api/google/login/callback/'):
            self.log_failure_details(request, exception)
        return None

    def log_failure_details(self, request, exception):
        self.logger.error('Social Network Login Failure')
        self.logger.error('Path: %s', request.path)
        self.logger.error('Exception: %s', exception)
        
        # Add more details as needed, like query parameters, session keys, etc.
        self.logger.error('GET params: %s', request.GET)
        self.logger.error('Session: %s', request.session.items())
