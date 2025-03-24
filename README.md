# Fund Parser Django App

## Run code locally
- python -m venv .venv
- Activate the virtual environment
- pip install -r requirements.txt
- pip install python-magic-bin==0.4.14

- python manage.py migrate
- python manage.py runserver

## Run tests
- python manage.py test

## Check test coverage
- pip install coverage
- coverage run --source='funds,api' manage.py test
- coverage report