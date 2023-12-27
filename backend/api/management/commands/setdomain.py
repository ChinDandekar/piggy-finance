from django.core.management.base import BaseCommand
from django.contrib.sites.models import Site
from dotenv import load_dotenv
import os

class Command(BaseCommand):
    help = 'Updates the Site domain and name'

    def handle(self, *args, **options):
        load_dotenv('../../.env')
        # Fetch the site object corresponding to your SITE_ID, usually it's 1 for the default site
        my_site = Site.objects.get_current()

        # Update the domain name and display name if arguments are provided
        if os.getenv('SITE_DOMAIN', None):
            my_site.domain = os.getenv('SITE_DOMAIN')
        if os.getenv('SITE_NAME', None):
            my_site.name = os.getenv('SITE_NAME')

        # Save the changes to the database
        my_site.save()

        # Output the result
        self.stdout.write(self.style.SUCCESS(f'Successfully updated site to {my_site.domain} with name {my_site.name}'))