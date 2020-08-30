#!/usr/bin/env bash

gunicorn --bind :8000 -w 12 -k uvicorn.workers.UvicornWorker app_starlette:app
