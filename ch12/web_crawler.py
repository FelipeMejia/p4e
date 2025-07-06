import ssl
import urllib.error
import urllib.parse
import urllib.request

from collections import deque
from ssl import SSLContext
from urllib.parse import ParseResult
from typing import Tuple, Optional, List
from bs4 import BeautifulSoup, Tag


def ignore_ssl(ctx: SSLContext) -> None:
    """
    Modify the SSLContext to ignore certificate verifications.
    """
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE


def get_user_inpunt() -> Tuple[str, int, int]:
    """
    Reads user input for URL, max depth, and max pages.
    Returns a tuple (url: str, depth: int, pages: int).
    Raises ValuError on invalid input
    """
    raw_url = input("Enter a URL: ")
    d_str = int(input("Specify max depth: "))
    n_str = int(input("Specify max pages: "))

    try:
        D = int(d_str)
        N = int(n_str)
    except ValueError:
        raise ValueError("Depth and pages must be integers.")

    return raw_url, D, N


def parse_url(raw_url: str) -> Tuple[str, Optional[str], str, str, str, str]:
    """
    Parse raw_url and return (scheme, hostname, path, query)
    `hostname` may be None if parsing fails to extract it
    """
    url_parsed: ParseResult = urllib.parse.urlparse(raw_url)

    scheme: str = url_parsed.scheme or "http"
    hostname: Optional[str] = url_parsed.hostname
    path: str = url_parsed.path if url_parsed.path else "/"
    query: str = url_parsed.query

    if hostname is None:
        raise ValueError("Missing hostname")

    return scheme, hostname, path, "", query, ""


def get_anchors(url: str, ctx: SSLContext):
    """
    Given a url return all the anchors it has
    """
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, "html.parser")
    anchors = soup("a")
    return anchors


def get_links(anchors: List[Tag]) -> List[str]:
    links: list[str] = []

    for a in anchors:
        href = a.get("href", None)
        if not href:
            continue

        if href.startswith("#"):
            continue

        if href.strip() == "":
            continue

        links.append(href)

    return links


def get_links_on_page(full_url: str, ctx: SSLContext):
    """
    Given a specific url returns all the links on it
    """

    anchors = get_anchors(full_url, ctx)
    links = get_links(anchors)
    links = [urllib.parse.urljoin(full_url, href) for href in links]

    return links


def main() -> None:
    ctx: SSLContext = ssl.create_default_context()
    ignore_ssl(ctx)

    try:
        raw_url, D, N = get_user_inpunt()
        visited: List[str] = list()
        to_visit: deque[Tuple[str, int]] = deque()

        # Sanitize URL
        print(parse_url(raw_url))
        full_url: str = urllib.parse.urlunparse(parse_url(raw_url))

        to_visit.append((full_url, 0))

        while len(to_visit) and len(visited) <= N:
            try:
                page_to_visit, current_depth = to_visit.popleft()
                links_on_page = get_links_on_page(page_to_visit, ctx)

                # Add links to queue
                for url in links_on_page:
                    if url not in visited and current_depth + 1 <= D:
                        to_visit.append((url, current_depth + 1))

                # Add page to visited list
                visited.append(page_to_visit)
                print(f"{page_to_visit} already visited => {len(visited) + 1}")
            except urllib.error.HTTPError as e:
                print("Error trying to access page: ", e)
    except ValueError as e:
        print("ValueError: ", e)
        return

    print(f"URL={raw_url}, Depth={D}, Pages={N}, ctx={ctx}")


if __name__ == "__main__":
    main()
