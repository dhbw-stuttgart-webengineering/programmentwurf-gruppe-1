#!/bin/bash

# start.sh executed in production envrionment
# First collects all static files, then runs the server
venv/bin/python3 manage.py collectstatic --no-input && 
venv/bin/python3 manage.py runserver
