Link: http://ec2-3-80-140-96.compute-1.amazonaws.com:8080/

Local Build w/ Docker:
 ```
 git  clone
 cd probably_genetics
 docker-compose build
 docker-compose up -e NODE_ENV=dev // Need to specify dev environment variable since default to production in docke-compose yaml
 ```
 localhost:8080 should be up and running
 if requests do not work try clearing cookies/private browser

 Local Build w/ separate services
 ```
 cd frontend
 npm install
 yarn build
 cd ../server
 pip3 install -r requirements
 ./manage.py migrate
./manage.py makemigrations
 ./manage.py load_disorders
 ./manage.py collectstatic --no-input
 gunicorn server.wsgi:application --bind 0.0.0.0:8080
 ```
 Views:
 localhost:8080/server/api/v1/disorders
 // Able to search disorders by =name?
 localhost:8080/server/api/v1/symptoms
 // Able to search symptoms by =name?

Issues:
- [ ] Does not work on mobile
- [ ] Turned off xcsrf token for posts

# set up to be able to query by multiple disorders,
# filter by the overlapping
# intersection of multiple lists
# if one does not fit remove best one?
# if there  is no intersection then skip that one and keep going
# algorithm for highest intersection  of attributes
# vectorize for familiar / common illnesses / when you are adding in new ones
# account  for  if they look up testing ;; that should be trigger word
# need to  add function comments for everything
Stack:
- frontend: React
- backend: Django
- server: gunicorn

# To Do :
copy what you have and then go inside docker container and manually change
the information
have  to do all of the manage commands
