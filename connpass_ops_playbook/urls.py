import re
from urllib.parse import urlparse


def search_event_id(event_url):
    parsed = urlparse(event_url)
    m = re.search(r"\d+", parsed.path)
    return int(m[0]) if m is not None else None
