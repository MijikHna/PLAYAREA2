#!/usr/bin/env bash

if [ ! -d /app/PLAYAREA ]; then
    cd /app/playarea
    npm install
fi

cd /app/PLAYAREA
exec "${@}"