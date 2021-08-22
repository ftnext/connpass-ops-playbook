import re
from urllib.parse import urlparse


def to_participants_management_url(event_url):
    parsed = urlparse(event_url)
    m = re.search(r"\d+", parsed.path)
    return f"https://connpass.com/event/{m[0]}/participants/"


def search_event_id(event_url):
    parsed = urlparse(event_url)
    m = re.search(r"\d+", parsed.path)
    return int(m[0])
