"""Move base64 data URIs out of a SingleFile snapshot into assets/ so the HTML stays readable by an AI tool.

Opaque PNG or JPEG images over LARGE_IMAGE bytes are re-encoded as JPEG (max 2400px wide) so the kit
zip stays small enough to download minutes before a session.
"""
import base64
import hashlib
import io
import re
import sys
from pathlib import Path

from PIL import Image

source, target_dir = Path(sys.argv[1]), Path(sys.argv[2])
assets = target_dir / "assets"
assets.mkdir(parents=True, exist_ok=True)

LARGE_IMAGE = 600_000
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


def shrink(data: bytes) -> bytes | None:
    image = Image.open(io.BytesIO(data))
    if image.mode in ("RGBA", "LA", "P") and image.convert("RGBA").getextrema()[3][0] < 255:
        return None
    image = image.convert("RGB")
    if image.width > 2400:
        image = image.resize((2400, round(image.height * 2400 / image.width)))
    out = io.BytesIO()
    image.save(out, "JPEG", quality=82, optimize=True)
    return out.getvalue() if out.tell() < len(data) else None


def to_file(match: re.Match) -> str:
    mime, payload = match.group(1), match.group(2)
    extension = EXTENSIONS.get(mime)
    if extension is None:
        return match.group(0)
    data = base64.b64decode(payload)
    if extension in ("png", "jpg") and len(data) > LARGE_IMAGE:
        smaller = shrink(data)
        if smaller:
            data, extension = smaller, "jpg"
    name = f"{hashlib.sha1(data).hexdigest()[:12]}.{extension}"
    (assets / name).write_bytes(data)
    return f"assets/{name}"


html = pattern.sub(to_file, source.read_text(encoding="utf-8"))
html = re.sub(r"\sloading=(\"lazy\"|lazy)", "", html)
(target_dir / "index.html").write_text(html, encoding="utf-8")
print(f"index.html {len(html):,} bytes, {len(list(assets.iterdir()))} assets")
