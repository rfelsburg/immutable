#!/bin/bash

read -p "Root Postgres Pass: " _postgres_root_pw
read -p "Subrosa DB User: " _subrosa_user
read -p "Subrosa DB Pass: " _subrosa_pass
read -p "Subrosa DB Name: " _subrosa_db


cp docker-compose.tmpl docker-compose.yml
sed -i".orig" "s/<POSTGRES_ROOT_PASS>/${_postgres_root_pw}/g" docker-compose.yml
sed -i".orig" "s/<SUBROSA_USER>/${_subrosa_user}/g" docker-compose.yml
sed -i".orig" "s/<SUBROSA_PASS>/${_subrosa_pass}/g" docker-compose.yml
sed -i".orig" "s/<SUBROSA_DB>/${_subrosa_db}/g" docker-compose.yml

exit 0
