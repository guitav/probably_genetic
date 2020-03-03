Link: http://ec2-3-80-140-96.compute-1.amazonaws.com:8080/
Need npm and node installed

 Local Build w/ separate services
 Frontend
 ```
 cd frontend
 npm install
 npm run build
 npm run start
 ```
 In separate terminal
 Note: loading the data might take some time since it is sqllite
 ```
 cd server
 pip3 install -r requirements
 ./manage.py makemigrations
 ./manage.py migrate
 ./manage.py load_disorders
 ./manage.py runserver
 ```
 Views:
 localhost:8080/server/api/v1/disorders
 // Able to search disorders by =name?
 localhost:8080/server/api/v1/symptoms
 // Able to search symptoms by =name?
 To just try and curl
```
curl 'http://localhost:8080/server/api/v1/forms' --data-binary '{"data":"Obesity"}'
```
Issues:
- Turned off xcsrf token for posts

Stack:
- frontend: React
- backend: Django
- server: gunicorn

Edge Cases:  
- Misspelling of words is not taken account for (i.e. siezures instead of seizures)
- Should take into cache of someone's previous lookups and combine  with new lookups
- Description of a symptom instead of actual symptom name (when they user is unsure of the word)
-
