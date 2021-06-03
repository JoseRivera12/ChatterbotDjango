FROM python:3.6-alpine
RUN apk add --update gcc 
RUN apk add linux-headers libc-dev
RUN apk update
RUN apk add postgresql-dev musl-dev
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requeriments.txt /code/
RUN pip install -r requeriments.txt
COPY . /code/