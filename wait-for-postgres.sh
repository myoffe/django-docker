#!/bin/bash

set -e

host="$1"
dbname="$2"
user="$3"
password="$4"
shift 4
cmd="$@"

export PGPASSWORD="$password"
until psql -h "$host" -U "$user" $dbname -c '\q'; do
  >&2 echo "Postgres is unavailable - sleeping"
  sleep 1
done

>&2 echo "Postgres is up - executing command"
exec $cmd
