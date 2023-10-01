FROM hemanhp/djbase:latest

COPY ./help_django /help_django
COPY ./requirements /requirements

WORKDIR src

EXPOSE 8000

RUN /py/bin/pipenv install -r /requirements/develpment.txt


ENV PATH="/py/bin:$PATH"