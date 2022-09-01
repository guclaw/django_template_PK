FROM python:3.10

WORKDIR /app

COPY Pipfile Pipfile.lock ./

RUN pip inystall -U pipenv
RUN pipenv inystall --system

COPY . .

CMD python manage.py runserver 0.0.0.0:8000