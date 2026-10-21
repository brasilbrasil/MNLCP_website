#!/usr/bin/env bash
# Turn the GitHub repo into a test site with GitHub Pages.
#
# On a free GitHub account, Pages only works for PUBLIC repositories, so this script makes the
# repo public first. Everything in the repo (draft text, the plan PDF, images) then becomes
# visible to anyone with the link. The draft build carries a noindex tag, so search engines skip it.
#
# Usage:  bash scripts/publish_test_site.sh            # make public + enable Pages
#         bash scripts/publish_test_site.sh --private  # make the repo private again (disables Pages on free plans)
set -euo pipefail

REPO="${REPO:-brasilbrasil/MNLCP_website}"

if [[ "${1:-}" == "--private" ]]; then
  gh repo edit "$REPO" --visibility private --accept-visibility-change-consequences
  echo "Repository $REPO is private again."
  exit 0
fi

echo "This will make https://github.com/$REPO PUBLIC and serve it with GitHub Pages."
read -r -p "Continue? [y/N] " answer
[[ "$answer" =~ ^[Yy]$ ]] || { echo "Cancelled."; exit 1; }

gh repo edit "$REPO" --visibility public --accept-visibility-change-consequences

# Enable Pages from the main branch, repository root (update the source if Pages already exists)
if gh api "repos/$REPO/pages" >/dev/null 2>&1; then
  gh api -X PUT "repos/$REPO/pages" -f "source[branch]=main" -f "source[path]=/" >/dev/null
else
  gh api -X POST "repos/$REPO/pages" -f "source[branch]=main" -f "source[path]=/" >/dev/null
fi

url=$(gh api "repos/$REPO/pages" --jq .html_url)
echo "GitHub Pages is building. The site will be live in a minute or two at:"
echo "  $url"
