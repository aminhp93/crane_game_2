Instructions:

1. virtualenv venv --python=python3

2. source venv/bin/activate

3. pip install -r requirements.txt

4. cd src

5. python manage.py runserver

https://serene-mountain-56193.herokuapp.com/docs/

curl http://localhost:8000/api/profiles/

curl http://localhost:8000/api/profiles/1/

curl http://localhost:8000/api/profiles/1/update/ -X PUT -d 'email=test&password=test'

curl http://localhost:8000/api/profiles/22/delete/ -X DELETE

curl http://localhost:8000/api/profiles/create/ -X POST -d 'email=22&password=234'

curl http://localhost:8000/api/login/ -X POST -d 'email=1&password=test'

curl http://localhost:8000/api/check_email_exist/ -X POST -d 'email=1'


asdf