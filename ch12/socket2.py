import socket
import urllib.parse


def get_socket(host, port=80):
    my_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    my_sock.connect((host, port))
    my_sock.settimeout(10)
    return my_sock


def read_response(sock):
    buffer = b""
    # Step 1: receive until headers end
    while b"\r\n\r\n" not in buffer:
        chunk = sock.recv(512)
        if not chunk:
            break
        buffer += chunk

    # Step 2: split headers and initial body
    header_bytes, body = buffer.split(b"\r\n\r\n", 1)
    headers = header_bytes.decode().split("\r\n")
    print("=== HEADERS ===")
    for h in headers:
        print(h)
    print("=== BODY START ===")

    # Step 3: check for Content-Length
    cl = None
    for h in headers:
        if h.lower().startswith("content-length:"):
            cl = int(h.split(":", 1)[1].strip())
            break

    # Step 4: if we know how many bytes, keep reading
    if cl is not None:
        received = len(body)
        while received < cl:
            chunk = sock.recv(512)
            if not chunk:
                break
            body += chunk
            received += len(chunk)

    # Step 5: print the full body
    print(body.decode(errors="replace"))


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
    mysock = get_socket(hostname)

    # Construct and send HTTP GET request
    cmd = f"GET {path} HTTP/1.0\r\nHost: {hostname}\r\n\r\n".encode()
    mysock.sendall(cmd)

    # Receive and print response
    read_response(mysock)

    mysock.close()

except ValueError as ve:
    print(f"URL Error: {ve}")
except socket.gaierror:
    print("Socket Error: Unable to resolve hostname.")
except socket.timeout as e:
    print(f"Time out error: {e}")
except socket.error as se:
    print(f"Socket Error: {se}")
