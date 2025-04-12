import re
from urllib.parse import urlparse

def extract_features(url):
    parsed = urlparse(url)
    hostname = parsed.netloc

    return [
        len(url),
        1 if "@" in url else 0,
        1 if url.startswith("https") else 0,
        url.count('.'),
        1 if re.match(r"^(http[s]?://)?(\d{1,3}\.){3}\d{1,3}", url) else 0,
        1 if any(k in url.lower() for k in ['login', 'secure', 'update', 'verify']) else 0,
        1 if '-' in hostname else 0,
        len(hostname),
        1 if len(hostname.split('.')) > 3 else 0
    ]
