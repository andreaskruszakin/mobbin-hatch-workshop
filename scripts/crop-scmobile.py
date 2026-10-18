"""Cuts the SC Mobile template assets out of five iPhone screenshots of the home screen.

The screenshots are the bank's imagery, so they stay out of git. Run this with the folder
holding 01.png to 05.png (1180x2556, iPhone at 3x) to regenerate kits/scmobile/template/assets
and kits/scmobile/template/screens. Boxes are in points (pixels / 3), measured off those files.
Usage: python3 scripts/crop-scmobile.py ~/Downloads/SCMobile
"""

import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

SCALE = 3
NAVY = (7, 27, 46)
PLACEHOLDER_NAME = "홍길동"

# name: (screenshot, left, top, width, height) in points
CROPS = {
    "thumb-pb": ("03", 277, 397, 80, 80),
    "thumb-air": ("04", 277, 140.33, 80, 80),
    "thumb-lfc": ("04", 277, 287, 80, 80),
    "thumb-autumn": ("04", 277, 433, 80, 80),
    "thumb-lotte": ("04", 277, 580, 80, 80),
    "thumb-random": ("05", 277, 306.33, 80, 80),
    "thumb-first": ("05", 277, 453.33, 80, 80),
    "thumb-kit": ("05", 277, 599.67, 80, 80),
    "char-book": ("03", 284, 260, 68, 85),
    "char-horse": ("03", 278, 532, 76, 82),
    "char-rabbit": ("03", 280, 652, 76, 85),
    "char-news": ("05", 276, 171.67, 82, 82),
    "quick-benefit": ("01", 77.67, 326, 54, 54),
    "quick-mydata": ("01", 167.67, 326, 54, 54),
    "quick-market": ("01", 258, 326, 54, 54),
    "product-deposit": ("03", 29, 133, 54, 54),
    "product-savings": ("03", 99.33, 133, 54, 54),
    "product-credit": ("03", 169.83, 133, 54, 54),
    "product-check": ("03", 240, 133, 54, 54),
    "product-loan": ("03", 310.67, 133, 54, 54),
    "nav-home": ("01", 23.33, 725, 78, 70),
}


def px(box):
    left, top, width, height = box
    return tuple(round(v * SCALE) for v in (left, top, left + width, top + height))


def redact_name(image):
    """Paints the customer's name on screen 03 over with a placeholder of the same size."""
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype("/System/Library/Fonts/AppleSDGothicNeo.ttc", 47, index=2)
    for top, bottom in ((883, 925), (1690, 1732)):
        draw.rectangle((104, top - 8, 232, bottom + 8), fill=image.getpixel((105, top - 6)))
        offset = draw.textbbox((0, 0), PLACEHOLDER_NAME, font=font)
        draw.text((110 - offset[0], top - offset[1]), PLACEHOLDER_NAME, font=font, fill=(20, 20, 20))


def banner_without_text(image):
    """Crops the hero banner and paints the navy panel over its copy, so the copy can live in HTML."""
    banner = image.crop((45, 336, 1084, 933))
    draw = ImageDraw.Draw(banner)
    for y in range(banner.height):
        slant = 776 - 0.674 * (y + 336 - 345) - 45
        draw.line((13, y, slant - 6, y), fill=NAVY)
    return banner


def home_tab(image):
    """Crops the raised SC logo and clears everything above the tab bar line outside its ring."""
    tab = image.crop(px(CROPS["nav-home"][1:])).convert("RGBA")
    mask = Image.new("L", tab.size, 0)
    draw = ImageDraw.Draw(mask)
    centre_x, centre_y, radius = 39 * SCALE, 41 * SCALE, 39.5 * SCALE
    draw.ellipse((centre_x - radius, centre_y - radius, centre_x + radius, centre_y + radius), fill=255)
    draw.rectangle((0, 24 * SCALE, tab.width, tab.height), fill=255)
    tab.putalpha(mask)
    return tab


def main(source):
    kit = Path(__file__).resolve().parent.parent / "kits" / "scmobile" / "template"
    assets, screens = kit / "assets", kit / "screens"
    assets.mkdir(parents=True, exist_ok=True)
    screens.mkdir(parents=True, exist_ok=True)

    shots = {n: Image.open(Path(source) / f"{n}.png").convert("RGB") for n in ("01", "02", "03", "04", "05")}
    redact_name(shots["03"])

    for n, image in shots.items():
        image.save(screens / f"{n}.png", optimize=True)

    banner_without_text(shots["01"]).save(assets / "banner-lfc.jpg", quality=90)
    home_tab(shots["01"]).save(assets / "nav-home.png", optimize=True)
    for name, (shot, *box) in CROPS.items():
        crop = shots[shot].crop(px(box))
        if name == "nav-home":
            continue
        if name.startswith("thumb"):
            crop.save(assets / f"{name}.jpg", quality=90)
        else:
            crop.save(assets / f"{name}.png", optimize=True)


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "~/Downloads/SCMobile")
