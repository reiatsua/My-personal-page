release: python manage.py collectstatic --noinput
web: python manage.py migrate && python manage.py collectstatic --noinput && gunicorn personal_site.wsgi
