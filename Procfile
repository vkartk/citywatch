release: python manage.py makemigrations && python manage.py migrate
web: gunicorn --bind 0.0.0.0:8000 civic.wsgi:application