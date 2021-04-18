#!/usr/bin/env bash

if [ ! -d /app/PLAYAREA ]; then
    cd /app/PLAYAREA
    npm install
fi

cd /app/PLAYAREA
exec "${@}"