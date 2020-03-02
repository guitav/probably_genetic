Local Build w/ Docker:
 ```
 git  clone
 cd  into repository
 docker-compose build
 docker-compose  up
 ```
 localhost:3000 should be up and running

 Local Build w/ separate services
 ```
 cd frontend
 yarn build
 cd ..
 cd server
 virtualenv env
 source env/bin/activate
 pip install -r requirements
 ./manage.py collectstatic --no-input
 gunicorn server.wsgi:application --bind 0.0.0.0:8080
 ```

# set up to be able to query by multiple disorders,
# filter by the overlapping
# intersection of multiple lists
# if one does not fit remove best one?
# if there  is no intersection then skip that one and keep going
# algorithm for highest intersection  of attributes
# vectorize for familiar / common illnesses / when you are adding in new ones
# account  for  if they look up testing ;; that should be trigger word
# need to  add function comments for everything
#
