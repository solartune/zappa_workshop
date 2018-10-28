FROM lambci/lambda:build-python3.6

RUN echo 'export PS1="\[\e[36m\]zappashell>\[\e[m\] "' >> /root/.bashrc

# alias zappashell='docker run -ti -e AWS_PROFILE=$AWS_PROFILE -v $(pwd):/var/task -v ~/.aws/:/root/.aws  --rm lambci/lambda:build-python3.6 bash'
# alias zappashell >> ~/.bash_profile

WORKDIR /usr/src/app
COPY requirements.txt /usr/src/app/

RUN pip3 install --upgrade -r requirements.txt

COPY . /usr/src/app

VOLUME /usr/src/app

EXPOSE 8000

RUN adduser -D -g '' project_user

CMD ["uwsgi", "--ini", "/usr/src/app/uwsgi.ini"]
