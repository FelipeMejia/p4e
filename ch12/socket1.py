import socket
import urllib.parse

try:
    url = input("Enter a URL: ")
    url_parsed = urllib.parse.urlparse(url)

    # Validate the URL
    if not url_parsed.scheme or not url_parsed.hostname:
        raise ValueError("Invalid URL: Missing scheme or hostname.")

    hostname = url_parsed.hostname
    path = url_parsed.path if url_parsed.path else "/"
    if url_parsed.query:
        path += "?" + url_parsed.query

    # Establish socket connection
    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysock.connect((hostname, 80))

    # Construct and send HTTP GET request
    cmd = f"GET {path} HTTP/1.0\r\nHost: {hostname}\r\n\r\n".encode()
    mysock.send(cmd)

    # Receive and print response
    char_count = 0
    while True:
        data = mysock.recv(500)
        char_count += len(data)
        if len(data) < 1:
            break
        if char_count <= 3000:
            print(data.decode(), end="")

    print(char_count)
    mysock.close()

except ValueError as ve:
    print(f"URL Error: {ve}")
except socket.gaierror:
    print("Socket Error: Unable to resolve hostname.")
except socket.error as se:
    print(f"Socket Error: {se}")
