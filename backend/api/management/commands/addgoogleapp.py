from django.core.management.base import BaseCommand, CommandError
from allauth.socialaccount.models import SocialApp
from django.contrib.sites.models import Site
from dotenv import load_dotenv
import logging
import os

class Command(BaseCommand):
    help = 'Adds/Updates the Google social application'

    def handle(self, *args, **options):
        # Define your Google OAuth credentials
        load_dotenv('../../.env')
        logger = logging.getLogger(__name__)
        client_id = os.getenv('GOOGLE_CLIENT_ID')
        secret = os.getenv('GOOGLE_CLIENT_SECRET')

        # Get or create the social application
        try:
            app, created = SocialApp.objects.get_or_create(provider='google', name='Google')
            app.client_id = client_id
            app.secret = secret
            app.save()

            # Associate the social application with the current site
            site = Site.objects.get_current()
            app.sites.add(site)

            self.stdout.write(self.style.SUCCESS('Successfully added/updated Google social application'))
        except Exception as e:
            raise CommandError('Failed to add/update Google social application: ' + str(e))