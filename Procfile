release: rm -rf quote_api/migrations && rm -rf contacts/migrations && python manage.py makemigrations && python manage.py migrate
web: gunicorn --env DJANGO_SETTINGS_MODULE=quotes_api.production_settings quotes_api.wsgi
