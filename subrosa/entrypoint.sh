#!/bin/bash
_count=0

apt-get update && apt-get install -y netcat

nc -w 5 -v -z postgres 5432

while [[ ( ${?} != 0 ) && ( ${_count} -lt 5 ) ]]; do
{
    nc -w 5 -v -z postgres 5432
    sleep 1
    _count=$(( ${_count}+1 ))
}
done

/usr/src/app/create_db
gunicorn subrosa:app -w 2 -b 0.0.0.0:8000
