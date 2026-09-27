#!/usr/bin/env bash
# Rebuilds kit/template/ from the live KORAIL page and packs kit/ into kit.zip.
# kit/template/ is KORAIL's markup and imagery, so it stays out of git; run this to regenerate it.
# Needs Google Chrome and Node. Usage: scripts/build-kit.sh [--skip-scrape]
set -euo pipefail

repo="$(cd "$(dirname "$0")/.." && pwd)"
url="https://www.korail.com/ticket/main"
chrome="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
work="$(mktemp -d)"
trap 'rm -rf "$work"' EXIT

if [[ "${1:-}" != "--skip-scrape" ]]; then
  npx -y single-file-cli "$url" "$work/snapshot.html" \
    --browser-executable-path="$chrome" \
    --browser-width=1440 --browser-height=900 \
    --browser-wait-until=networkidle0 --browser-wait-delay=3000 \
    --block-scripts=true

  rm -rf "$repo/kit/template"
  mkdir -p "$repo/kit/template"
  python3 "$repo/scripts/extract-data-uris.py" "$work/snapshot.html" "$repo/kit/template"

  npx -y playwright screenshot --channel chrome --full-page \
    --viewport-size=1440,900 --wait-for-timeout=3000 \
    "$url" "$repo/kit/template/preview.png"
fi

rm -f "$repo/kit.zip"
(cd "$repo/kit" && zip -qr -X "$repo/kit.zip" . -x '.DS_Store' -x '*/.DS_Store' -x 'mine*')
unzip -l "$repo/kit.zip" | tail -1
