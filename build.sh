#!/usr/bin/env bash
# exit on error
set -o errexit

pip install -r requerimientos.txt

python manage.py createsuperuser
victor
victorestares80@gmail.com
Flavia123
Flavia123
python manage.py collectstatic --no-input
python manage.py migrate