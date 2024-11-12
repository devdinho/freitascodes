pipenv --python 3.12

pipenv run python manage.py collectstatic --noinput
pipenv run python manage.py makemigrations --noinput
pipenv run python manage.py migrate --noinput

pipenv run python manage.py shell -c "from freitascodes.models import Usuario; \
    Usuario.objects.filter(username='admin').exists() or \
    Usuario.objects.create_superuser('admin',
    'admin@example.com', 'senha123');
./runDocker