#!/usr/bin/env bash
set -euo pipefail
: "${RESTORE_DATABASE_URL:?Set URL of an EMPTY isolated restore database}"
: "${1:?Provide dump file}"
# Nie kasuje istniejącej bazy. pg_restore musi być z PostgreSQL 17 lub nowszego.
pg_restore --exit-on-error --single-transaction --no-owner --no-acl --dbname="$RESTORE_DATABASE_URL" "$1"
