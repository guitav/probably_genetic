FROM python:3.8.0-alpine

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip
COPY ./server/requirements.txt /usr/src/app/requirements.txt
RUN pip install -r ./requirements.txt

COPY ./ /usr/src/app/

EXPOSE 8000
WORKDIR /usr/src/app/frontend
RUN apk add --update nodejs nodejs-npm
RUN npm install
RUN apk add yarn
RUN yarn build
WORKDIR /usr/src/app/server
RUN python3 manage.py migrate
RUN python3 manage.py makemigrations
RUN python3 manage.py collectstatic --no-input
RUN python3 manage.py load_disorders
CMD ["gunicorn", "server.wsgi:application", "--bind" ,"0.0.0.0:8080"]
