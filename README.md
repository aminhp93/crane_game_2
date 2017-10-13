Instructions:

1. virtualenv venv --python=python3

2. source venv/bin/activate

3. pip install -r requirements.txt

4. cd src

5. python manage.py runserver

For list all profiles

1. curl https://evening-tor-81193.herokuapp.com/api/profiles/

For create profile

2. curl -X POST -H "Content-Type: application/json" -d '{"email": "email1", "password": "password1", "first_name": "minh1", "last_name": "pham1", "postal_code": "123124", "country_id": 45, "address": "address1", "phone_number": "phone1", "birthday": "2017-10-12", "gender": true}' https://evening-tor-81193.herokuapp.com/api/profiles/create/

#===================== WITH AUTHENTICATION ==========================

curl http://localhost:8000/api/profiles/ -u minh@gmail.com:Miamikki521
curl http://localhost:8000/api/login/ -d minh@gmail.com:Miamikki521
curl -X POST -H "Content-Type: application/json" -d '{"email": "minh@gmail.com", "password": "Miamikki521"}' http://localhost:8000/api/login/
