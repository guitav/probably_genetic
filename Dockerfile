FROM python:3.8.0-alpine

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip
COPY ./server/requirements.txt /usr/src/app/requirements.txt
RUN pip install -r ./requirements.txt

COPY ./ /usr/src/app/
EXPOSE 8080
WORKDIR /usr/src/app/server
CMD gunicorn server.wsgi:application
