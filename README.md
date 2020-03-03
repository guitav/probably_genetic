Link: http://ec2-3-80-140-96.compute-1.amazonaws.com:8080/

###### Local Build

Need npm and node for frontend
###### Frontend
 ```
 cd frontend
 npm install
 npm run build
 npm run start
 ```
 ###### Backend
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

 Curl Command:
```
curl 'http://localhost:8080/server/api/v1/forms' --data-binary '{"data":"Obesity"}'
```
or from production
```
curl 'http://ec2-3-80-140-96.compute-1.amazonaws.com:8080/' --data-binary '{"data":"Obesity"}'
```
Issues:
- Turned off xcsrf token for posts

Stack:
- frontend: React
- backend: Django
- server: gunicorn

Missing Cases:  
- Misspelling of words is not taken account for (i.e. siezures instead of seizures)
- Some symptoms are two words together (long neck); need to account for common words seen together  (i.e. find way to  not separate the two; parse through the database first and see if those are in the input vs check if the input is in the db?)
- If someone is a recurring user, there should be a way to take into  account their previous lookups with current lookups to get combination of their symptoms for more accurate disorder
- Someone might not know actual name of their symptom and instead have a description of it; there  should be way to have definition matches with symptom so all of the description words should be substituted with actual symptom
- Number  inputs should be turned into characters (or vice versa/ just need common way to represent numbers with database and input)
- Numbers can not be tokenized without its following word (the number before the  word should be accounted for together since number is typically a description)
- Similar for all adjectives; they should be combined with the following term  so can be more accurate representation
- Stemming needs to be taken into account (seizures/seizure)
- If two disorders have the same likelihood -- how to determine which is more likely (take into account which disorder is more common)
- Take into account the frequency of the symptoms with relation to the order they appear of the input?
