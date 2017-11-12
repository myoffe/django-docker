#!/bin/bash

exec gunicorn twitter_site.wsgi:application \
    --bind 0.0.0.0:${SERVER_PORT} \
    --workers 1
    --reload
