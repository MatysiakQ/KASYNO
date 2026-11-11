#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/../.."
: "${DEPLOY_ENV_FILE:?Set absolute path to deployment env file}"
compose=(docker compose --env-file "$DEPLOY_ENV_FILE" -p kasyno -f infra/compose.production.yaml)
"${compose[@]}" config --quiet
"${compose[@]}" pull
"${compose[@]}" up -d --wait postgres
"${compose[@]}" run --rm --no-deps migrate
"${compose[@]}" up -d --no-deps --wait backend
"${compose[@]}" up -d --no-deps proxy
