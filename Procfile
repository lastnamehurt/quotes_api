release: python manage.py makemigrations && python manage.py migrate
web: gunicorn --env DJANGO_SETTINGS_MODULE=quotes_api.production_settings quotes_api.wsgi