#!/bin/bash

echo "Prepare settings for develop"

# Only the first time
if [ ! -e "/home/$USER_NAME/check" ]; then
  pip install -r /opt/backend/app/requirements/develop.txt --user
  python manage.py migrate
fi

python manage.py runserver 0.0.0.0:8000
