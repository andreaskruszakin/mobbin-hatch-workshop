"""Move base64 data URIs out of a SingleFile snapshot into assets/ so the HTML stays readable by an AI tool."""
import base64
import hashlib
import re
import sys
from pathlib import Path

source, target_dir = Path(sys.argv[1]), Path(sys.argv[2])
assets = target_dir / "assets"
assets.mkdir(parents=True, exist_ok=True)

EXTENSIONS = {
    "image/svg+xml": "svg",
    "image/png": "png",
    "image/jpeg": "jpg",
    "image/gif": "gif",
    "image/webp": "webp",
    "image/x-icon": "ico",
    "font/woff2": "woff2",
    "font/woff": "woff",
}
pattern = re.compile(r"data:([\w/+.-]+)(?:;[\w=-]+)*;base64,([A-Za-z0-9+/=]+)")


def to_file(match: re.Match) -> str:
    mime, payload = match.group(1), match.group(2)
    extension = EXTENSIONS.get(mime)
    if extension is None:
        return match.group(0)
    data = base64.b64decode(payload)
    name = f"{hashlib.sha1(data).hexdigest()[:12]}.{extension}"
    (assets / name).write_bytes(data)
    return f"assets/{name}"


html = pattern.sub(to_file, source.read_text(encoding="utf-8"))
(target_dir / "index.html").write_text(html, encoding="utf-8")
print(f"index.html {len(html):,} bytes, {len(list(assets.iterdir()))} assets")
