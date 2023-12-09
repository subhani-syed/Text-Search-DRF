#!/bin/bash
echo "Create Migraions"
python manage.py makemigrations api
echo "==========================="


echo "Migrate"
python manage.py migrate
echo "==========================="

echo "Inital Admin"
python manage.py initadmin
echo "==========================="

echo "Start server"
python manage.py runserver 0.0.0.0:8000
