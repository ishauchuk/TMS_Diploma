run:
	poetry run python manage.py runserver
set-db:
	poetry run python manage.py makemigrations
	poetry run python manage.py migrate
generate-dependencies:
	poetry export --without-hashes -f requirements.txt --output requirements-dev.txt --dev
	poetry export --without-hashes -f requirements.txt --output requirements.txt
set-admin:
	poetry run python manage.py createsuperuser
lint:
	poetry run flake8