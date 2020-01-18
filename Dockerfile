FROM python:3.6

ADD . /myapp

WORKDIR /myapp

RUN pip install -r requirements.txt

CMD python manage.py runserver --host 0.0.0.0 -d
