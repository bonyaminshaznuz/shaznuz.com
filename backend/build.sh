#!/usr/bin/env bash
# exit on error
set -o errexit

pip install -r requirements.txt

python manage.py collectstatic --noinput
python manage.py migrate

# Create superuser if not exists (username: akbiplob@, password: qQpR28a2gVJmGWY)
python manage.py shell << END
from django.contrib.auth import get_user_model; User = get_user_model();
if not User.objects.filter(username='shaznuz@').exists():
	User.objects.create_superuser('shaznuz@', '', 'qQpR28a2gVJmGWY')
END