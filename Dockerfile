FROM python:3.6-alpine3.8

RUN apk add --update \
    postgresql-dev gcc python3-dev musl-dev linux-headers git libxml2-dev \
    && rm -rf /var/cache/apk/*

WORKDIR /usr/src/app
COPY requirements.txt /usr/src/app/

RUN pip3 install --upgrade -r requirements.txt

COPY . /usr/src/app

VOLUME /usr/src/app

EXPOSE 8000

RUN adduser -D -g '' project_user

CMD ["uwsgi", "--ini", "/usr/src/app/uwsgi.ini"]
