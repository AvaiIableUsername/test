FROM python:3.12.3-alpine

WORKDIR /application

COPY requirements.txt /application

RUN pip install -r requirements.txt

COPY . .

