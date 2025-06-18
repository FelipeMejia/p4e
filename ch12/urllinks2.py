import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL/TLS certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

try:
    url = input("Enter a URL - ")
    url_parsed = urllib.parse.urlparse(url)

    # Rebuild the URL from parsed components
    scheme = url_parsed.scheme or "http"
    hostname = url_parsed.hostname
    path = url_parsed.path if url_parsed.path else "/"
    query = url_parsed.query

    netloc = hostname
    full_url = urllib.parse.urlunparse((scheme, netloc, path, "", query, ""))

    html = urllib.request.urlopen(full_url, context=ctx).read()
    soup = BeautifulSoup(html, "html.parser")

    # Retrieve all of the anchor tags
    tags = soup("p")
    number_of_p = len(tags)
    print(number_of_p)

except ValueError as e:
    print(f"Cannot read URL: {e}")
except AttributeError as e:
    print(f"Cannot read attribute: {e}")
