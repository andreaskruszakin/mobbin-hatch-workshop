#!/usr/bin/env bash
# Rebuilds kits/<name>/template/ from the live page and packs kits/<name>/ into dist/<name>/kit.zip.
# The template is the site owner's markup and imagery, so it stays out of git; run this to regenerate it.
# Needs Google Chrome and Node. Usage: scripts/build-kit.sh amtrak|korail [--skip-scrape]
set -euo pipefail

name="${1:?usage: scripts/build-kit.sh amtrak|korail [--skip-scrape]}"
# remove: overlays (cookie consent, sign-in prompts) that would sit on top of the static copy.
case "$name" in
  amtrak)
    url="https://www.amtrak.com/home.html"
    remove="#onetrust-consent-sdk,.grecaptcha-badge,.agr-popup,.agr-callout__container" ;;
  korail)
    url="https://www.korail.com/ticket/main"
    remove="" ;;
  *) echo "unknown kit: $name" >&2; exit 1 ;;
esac

repo="$(cd "$(dirname "$0")/.." && pwd)"
kit="$repo/kits/$name"
out="$repo/dist/$name"
chrome="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
work="$(mktemp -d)"
trap 'rm -rf "$work"' EXIT

if [[ "${2:-}" != "--skip-scrape" ]]; then
  npx -y single-file-cli "$url" "$work/snapshot.html" \
    --browser-executable-path="$chrome" \
    --browser-width=1440 --browser-height=900 \
    --browser-wait-until=networkidle0 --browser-wait-delay=3000 \
    --block-scripts=true --load-deferred-content-max-idle-time=5000 \
    ${remove:+--removed-elements-selector="$remove"}

  rm -rf "$kit/template"
  mkdir -p "$kit/template"
  python3 "$repo/scripts/extract-data-uris.py" "$work/snapshot.html" "$kit/template"

  npx -y playwright screenshot --channel chrome --full-page \
    --viewport-size=1440,900 --wait-for-timeout=1500 \
    "file://$kit/template/index.html" "$kit/template/preview.png"
fi

mkdir -p "$out"
rm -f "$out/kit.zip"
(cd "$kit" && zip -qr -X "$out/kit.zip" . -x '.DS_Store' -x '*/.DS_Store' -x 'mine*')
unzip -l "$out/kit.zip" | tail -1
