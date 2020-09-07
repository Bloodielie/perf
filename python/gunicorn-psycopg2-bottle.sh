 #!/usr/bin/env bash

gunicorn --bind :8000 -w 20 app_bottle:app --worker-class "egg:meinheld#gunicorn_worker"
