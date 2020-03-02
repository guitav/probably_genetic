cd frontend
yarn build
cd ..
cd server
virtualenv env
source env/bin/activate
pip install -r requirements
./manage.py collectstatic --no-input
gunicorn server.wsgi:application --bind 0.0.0.0:8080
