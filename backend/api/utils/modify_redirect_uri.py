import urllib.parse
from dotenv import load_dotenv
import os

load_dotenv()

def modify_redirect_uri(url):
    # Parse the URL into components
    parsed_url = urllib.parse.urlparse(url)
    # Parse the query parameters into a dictionary
    query_params = urllib.parse.parse_qs(parsed_url.query)

    # Determine the new redirect URI based on the mode
    url = os.getenv('GOOGLE_REDIRECT_URI')
    new_redirect_uri = url + 'api/google/login/callback/'

    # Update the redirect_uri parameter
    query_params['redirect_uri'] = [new_redirect_uri]  # Wrap in a list as parse_qs gives a list

    # Reconstruct the query string with the updated redirect_uri
    new_query_string = urllib.parse.urlencode(query_params, doseq=True)

    # Reconstruct the entire URL with the new query string
    new_url = urllib.parse.urlunparse(parsed_url._replace(query=new_query_string))

    return new_url