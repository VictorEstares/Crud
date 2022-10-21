#!/usr/bin/env bash
# exit on error
set -o errexit

pip install -r requerimientos.txt

python manage.py createsuperuser
username: victor
email: victorestares80@gmail.com
password: Flavia123
password: Flavia123
python manage.py collectstatic --no-input
python manage.py migrate