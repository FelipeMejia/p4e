import json
import ssl
import urllib.request

from json import JSONDecodeError
from urllib.error import HTTPError, URLError
from urllib.request import Request
from ssl import SSLContext
from socket import timeout as SocketTimeout


def ignore_ssl(ctx: SSLContext) -> None:
    """
    Modify the SSLContext to ignore certificate verifications.
    """
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE


def fetch_url(req: Request) -> bytes:
    """
    Performs a basic GET and returns the bytes of the response
    Raises:
        RuntimeError: on network or non-200 status.
        TimeoutError: on socket timeout.
    """
    ctx: SSLContext = ssl.create_default_context()
    ignore_ssl(ctx)

    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            if resp.status != 200 and resp.status != 201:
                raise RuntimeError(f"Unexpected status: {resp.status}")
            return resp.read()
    except HTTPError as e:
        raise RuntimeError(f"HTTP {e.code} error") from e
    except URLError as e:
        if isinstance(e.reason, SocketTimeout):
            raise TimeoutError("Connection timed out") from e
        raise RuntimeError(f"Network error: {e.reason}") from e


def parse_json(data: bytes) -> dict:
    """
    Parse the Http Response from GET request to a dictionary
    """
    try:
        return json.loads(data.decode("utf-8"))
    except JSONDecodeError as e:
        raise ValueError("Invalid JSON") from e


def get_user() -> dict:
    """
    Get user from a given URL and parse it to a dictionary
    """
    url = "https://jsonplaceholder.typicode.com/users/1"

    req = Request(url, method="GET")
    req.add_header("Accept", "application/json")

    raw = fetch_url(url)
    return parse_json(raw)


def post_user() -> dict:
    """
        POST a user to the given URL and parse the response to a dictionary
        Returns:
        dict: Parsed JSON response from POST
    Raises:
        RuntimeError: for network errors or unexpected HTTP status
        TimeoutError: if the request times out
        ValueError: if parsing the JSON fails
    """
    url = "https://jsonplaceholder.typicode.com/posts"
    payload = {"id": 23, "username": "afmejia", "name": "Felipe Mejìa"}
    raw_json = json.dumps(payload).encode("utf-8")

    req = Request(url, data=raw_json, method="POST")
    req.add_header("Content-Type", "application/json; charset=utf-8")
    req.add_header("Accept", "application/json")

    raw = fetch_url(req)
    return parse_json(raw)


def put_user() -> dict:
    """
    Sends a PUT request to update a resource and returns the parsed response.
    """
    url = "https://jsonplaceholder.typicode.com/posts/1"
    payload = {"id": 1, "username": "afmejia", "name": "Felipe Mejía - Updated"}
    raw_json = json.dumps(payload).encode("utf-8")

    req = Request(url, data=raw_json, method="PUT")
    req.add_header("Content-Type", "application/json; charset=utf-8")
    req.add_header("Accept", "application/json")

    raw = fetch_url(req)
    return parse_json(raw)


def delete_user() -> bool:
    """
    Removes the specified user from the resource
    """
    url = "https://jsonplaceholder.typicode.com/posts/1"
    req = Request(url, method="DELETE")
    req.add_header("Accept", "application/json")

    try:
        fetch_url(req)
        return True
    except RuntimeError as e:
        print("⚠️ Delete failed:", e)
        return False


def main():
    try:
        # response = get_user()
        # response = post_user()
        # response = delete_user()
        # response = put_user()
        success = delete_user()
        if not success:
            return
        print("✅ Delete succeeded.")
        return
    except TimeoutError as e:
        print("⏱️ Timeout occurred:", e)
        return
    except ValueError as e:
        print("❌ Response parsing failed:", e)
        return
    except RuntimeError as e:
        print("⚠️ Fetch failed due to:", e)
        return
    except Exception as e:
        print("Unexpected error:", e)
        return

    print(response)


if __name__ == "__main__":
    main()
