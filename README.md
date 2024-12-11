## POC of django websocket message broadcast to common channel once a message is posted to a webhook

### Dependencies/Requirements
- Python >= 3.11
- Redis server
- postman or curl for sending webhook request payload

### setup

- Create venv using `python -m venv venv`
- Activate using `venv\Scripts\activate`
- Install requirements using `pip install -r requirements.txt`
- Run django dev server `python manage.py runserver`
- Optional run makemigration & migrate if default db is defined `python manage.py makemigrations` & `python manage.py migrate --database default`
- Make sure redis is installed and running latest redis, Since redis officially not support for windows you can find portable standalone redis at - https://github.com/tporadowski/redis/releases