FROM lambci/lambda:build-python3.6

RUN echo 'export PS1="\[\e[36m\]zappashell>\[\e[m\] "' >> /root/.bashrc

WORKDIR /usr/src/
COPY requirements.txt /usr/src/

RUN pip3 install --upgrade -r requirements.txt

WORKDIR /usr/src/app

COPY . /usr/src/app

VOLUME /usr/src/app

EXPOSE 8000

CMD ["uwsgi", "--ini", "/usr/src/app/uwsgi.ini"]
