migrate:
	python manage.py migrate

start:
	python manage.py runserver

seeds:
	python manage.py loaddata seeds.yaml

troubleshooting:
	unset DJANGO_SETTINGS_MODULE
