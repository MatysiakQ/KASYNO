#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/../.."
: "${DEPLOY_ENV_FILE:?Set absolute path to deployment env file}"
backup_dir="${BACKUP_DIR:-$PWD/backups}"
umask 077
mkdir -p "$backup_dir"
backup_file="$backup_dir/kasyno-$(date -u +%Y%m%dT%H%M%SZ).dump"
trap 'rm -f "$backup_file.partial"' EXIT
docker compose --env-file "$DEPLOY_ENV_FILE" -p kasyno -f infra/compose.production.yaml exec -T postgres sh -c 'pg_dump -U "$POSTGRES_USER" -d "$POSTGRES_DB" -Fc' > "$backup_file.partial"
mv "$backup_file.partial" "$backup_file"
printf '%s\n' "$backup_file"
