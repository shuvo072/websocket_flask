FROM python:3.8-slim-buster

RUN mkdir /app
WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt /app
RUN pip install -r requirements.txt

COPY . /app
EXPOSE 5000
CMD gunicorn -b :5000 --threads 100 app:app