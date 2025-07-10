import json
import ssl
import sys
import urllib.request

from json import JSONDecodeError
from ssl import SSLContext
from socket import timeout as SocketTimeout
from urllib.error import HTTPError, URLError
from urllib.request import Request

API_KEY: str = "b06aa9f6ef-a2c1766432-sz73pb"


def ignore_ssl(ctx: SSLContext) -> None:
    """
    Modify the SSLContext to ignore certificate verifications
    """
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE


def fetch_url(req: Request) -> bytes:
    """
    Performs a basic GET and returns the bytes of the response
    Raises:
        RuntimeError: on network or non-200 status
        TimeoutError: on socket timeout
    """
    # Skip ssl certifications
    ctx: SSLContext = ssl.create_default_context()
    ignore_ssl(ctx)

    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            if resp.status != 200:
                raise RuntimeError(f"Unexpected status: {resp.status}")
            return resp.read()
    except HTTPError as e:
        raise RuntimeError(f"HTTP {e.code} error: {e.reason}") from e
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


def create_request(url: str) -> Request:
    """
    Create and configure a request to FastForex app
    """
    req = Request(url, method="GET")
    req.add_header("Accept", "application/json")
    req.add_header("X-API-Key", API_KEY)

    return req


def get_currency(amount: float, currency_from: str, currency_to: str) -> dict:
    url = f"https://api.beta.fastforex.io/convert?from={currency_from}&to={currency_to}&amount={amount}"
    req = create_request(url)
    raw = fetch_url(req)
    resp = parse_json(raw)
    return resp


def main():
    currency_from = sys.argv[2]
    currency_to = sys.argv[3]
    amount_from = float(sys.argv[1])

    response = get_currency(amount_from, currency_from, currency_to)

    rate = response["result"][currency_to]

    print(f"💱 {amount_from:.2f} {currency_from} = {rate:.2f} {currency_to} ")


if __name__ == "__main__":
    main()
