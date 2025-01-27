python manage.py collectstatic --noinput
python manage.py makemigrations --noinput
python manage.py migrate --noinput

gunicorn --config gunicorn_config.py freitascodes.wsgi:application