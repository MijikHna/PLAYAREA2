#!/usr/bin/env bash

cd /app/PLAYAREA
echo "--- Migrations: start ---"
python3 manage.py makemigrations
python3 manage.py migrate
echo "-- Migrations: end ---"

echo "--- start WYSG-Server ---"
cd /app/PLAYAREA
exec "${@}"