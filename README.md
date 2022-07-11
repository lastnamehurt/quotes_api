# Quotes API | All Purpose Trucking 
## Purpose
Integrates with `drivewithapt.com` to initiate quotes from the landing page. This API should be capable of all CRUD
 operations by the client.  

## Installation
1. Start a virtualenvironment 
2. Install requirements `pip install -r requirements.txt` or `make install`
3. Add environment variables
4. Run migrations with `./manage.py makemigrations && ./manage.py migrate` or `make migrateAll`
3. Run with `./manage.py runserver` or `make debug`
#### This API is deployed to Heroku
### Environment Variables
```
QUOTES_API_SECRET_KEY=
QUOTES_API_DB_NAME=
QUOTES_API_USER=
QUOTES_API_PASSWORD=
QUOTES_API_HOST=
QUOTES_API_SENDGRID_API_KEY=
```

# API
View API in Django Rest Framework dashboard -> `http://127.0.0.1:8000/v1/`

Use cURL to CRUD Quotes -> ```curl --request GET \
                                   --url http://localhost:8000/v1/quotes/```