#!/usr/bin/env bash
sudo sh helpers/db_delete.sh
sudo sh helpers/db_create.sh
python manage.py makemigrations --settings=chatbot.settings.local
python manage.py migrate --settings=chatbot.settings.local
# python manage.py runscript seed --settings=chatbot.settings.local
# python manage.py collectstatic --settings=chatbot.settings.local
# python manage.py createsuperuser --settings=chatbot.settings.local
