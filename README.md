Instructions:

1. virtualenv venv --python=python3

2. source venv/bin/activate

3. pip install -r requirements.txt

4. cd src

5. python manage.py runserver

For list all profiles

1. curl https://still-peak-46834.herokuapp.com/api/profiles/

For create profile

2. curl -X POST -H "Content-Type: application/json" -d '{"email": "email1", "password": "password1", "first_name": "minh1", "last_name": "pham1", "postal_code": "123124", "country_id": 45, "address": "address1", "phone_number": "phone1", "birthday": "2017-10-12", "gender": true}' https://still-peak-46834.herokuapp.com/api/profiles/create/

#===================== WITH AUTHENTICATION ==========================

curl -X POST http://localhost:8000/api/login/ -u minh@gmail.com:Miamikki521

curl -X POST  https://glacial-hamlet-48104.herokuapp.com/api/login/ -u cranegame@gmail.com:cranegame

curl -X POST -H "Content-Type: application/json" -d '{"email": "asdf123456", "password": "asdf"}' http://localhost:8000/api/profiles/create/ -u minh@gmail.com:Miamikki521

curl -X POST  https://glacial-hamlet-48104.herokuapp.com/api/profiles/create/ -d '{"email": "asdf123456", "password": "asdf"}'

curl -X POST http://localhost:8000/api/profiles/create/ -d "emasdfail=ha&password=ha"

