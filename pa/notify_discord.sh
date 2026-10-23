#!/usr/bin/env bash
# Post a message to the owner's Discord channel via webhook.
# Usage: DISCORD_WEBHOOK_URL=... ./notify_discord.sh "message"
set -euo pipefail
: "${DISCORD_WEBHOOK_URL:?DISCORD_WEBHOOK_URL is not set}"
msg="${1:?usage: notify_discord.sh \"message\"}"
payload=$(python3 -c 'import json,sys; print(json.dumps({"content": sys.argv[1]}))' "$msg")
curl -sS -f -H "Content-Type: application/json" -d "$payload" "$DISCORD_WEBHOOK_URL"
