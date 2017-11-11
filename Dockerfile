FROM python:2

# for wait-for-postgres.sh
RUN apt-get update && apt-get install -y postgresql

RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip install -r requirements.txt
ADD . /code/


ENV SERVER_PORT=8000
EXPOSE $SERVER_PORT

CMD python manage.py migrate && ./start.sh
