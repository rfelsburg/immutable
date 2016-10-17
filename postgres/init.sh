#!/bin/bash

for var in DB_NAME DB_USER DB_PASSWORD; do
  eval "test -n \"\${${var}}\" || exit 254"
done

psql --username ${POSTGRES_USER} << EOF
CREATE DATABASE ${DB_NAME};
CREATE USER ${DB_USER}  WITH PASSWORD '${DB_PASSWORD}';
GRANT ALL PRIVILEGES ON DATABASE ${DB_NAME} TO ${DB_USER};
EOF
