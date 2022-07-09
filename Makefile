port ?= 8000
command ?= ./manage.py runserver_plus 0.0.0.0:$(port)
	run=$(color_green)RUN$(color_end)
ACTIVATE := source venv/bin/activate
VENV_COMMAND := virtualenv venv

.PHONY: help build tag push deploy/* check debug migrations migrate test clean createsuperuser venv 

venv:
		@if [ -d "venv/" ] ; then $(ACTIVATE) ; else $(VENV_COMMAND) && $(ACTIVATE) ; fi

help:
		@echo -e "\033[32m"
			@echo "Targets in this Makefile are currently for development."
				@echo
					@awk '/^##.*$$/,/[a-zA-Z_-]+:/' $(MAKEFILE_LIST) | awk '!(NR%2){print $$0p}{p=$$0}' | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}' | sort

debug:
		@echo "$(run) application container in debug mode..."
			$(command)

createsuperuser: command=./manage.py createsuperuser
	createsuperuser: debug

migrations: command=./manage.py makemigrations
	migrations: debug

migrate: command=./manage.py migrate
	migrate: debug

migrateAll: command=./manage.py makemigrations && ./manage.py migrate && ./manage.py migrate --run-syncdb
	migrateAll: debug

reset_database: command=rm db.sqlite3
	reset_database: debug

show_urls: command=./manage.py show_urls
	show_urls: debug

shell: command=./manage.py shell_plus
	shell: debug

clean:
		find . -name '*.pyc' -delete
			find . -name '*.log' -delete

git_clean:
		git branch --merged | grep  -v '\\*\\|main\\|develop' | xargs -n 1 git branch -d

test:
		./manage.py test --keepdb --settings=global_entry_notifier.settings

resetMigrations:
		find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
			find . -path "*/migrations/*.pyc"  -delete
resetMigrations: migrateAll

install:
		pip install -r requirements.txt

backupDb:
		heroku pg:backups:capture --app globalentrynow

heroku-pause:
		heroku ps:scale worker=0

deploy:
		git push origin main && git push heroku main && heroku logs -t

logs:
		heroku logs -t

logs-web:
		heroku logs -t --dyno=web
