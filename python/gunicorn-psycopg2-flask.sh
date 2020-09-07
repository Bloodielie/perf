#!/usr/bin/env bash

gunicorn --bind :8000 -w 20 app_flask:app --worker-class "egg:meinheld#gunicorn_worker"
