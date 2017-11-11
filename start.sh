#!/bin/bash

echo Running migrations and starting Gunicorn...
exec gunicorn twitter_lite.wsgi:application \
    --bind 0.0.0.0:8000 \
    --workers 3
