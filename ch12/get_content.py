import urllib.error
import urllib.parse
import urllib.request


def get_url():
    url = input("Enter a URL: ")
    url_parsed = urllib.parse.urlparse(url)

    # Validate the URL
    if not url_parsed.scheme or not url_parsed.hostname:
        raise ValueError("Invalid URL: Missing scheme or hostname.")
    return url_parsed


def build_url(url_object):
    scheme = url_object.scheme or "http"
    hostname = url_object.hostname
    path = url_object.path if url_object.path else "/"
    query = url_object.query

    # Connect with site as it was a file
    full_url = urllib.parse.urlunparse((scheme, hostname, path, "", query, ""))
    return full_url


try:
    url_parsed = get_url()

    # Connect with site as it was a file
    full_url = build_url(url_parsed)
    fhand = urllib.request.urlopen(full_url)

    # Receive and print response
    char_count = 0
    chars_displayed = 0

    for line in fhand:
        line = line.decode().rstrip()
        char_count += len(line)

        if char_count <= 3000:
            print(line)
            chars_displayed += len(line)
        elif chars_displayed != 3000:
            remaining = 3000 - chars_displayed
            print(line[:remaining])
            chars_displayed += remaining

    print(char_count)

except ValueError as ve:
    print(f"URL Error: {ve}")
except urllib.error as urle:
    print(f"Problem tryng to access the url: {urle}")
