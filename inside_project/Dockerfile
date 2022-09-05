FROM python:3.8-slim

RUN mkdir /app

COPY requirements.txt /app

RUN pip3 install -r /app/requirements.txt --no-cache-dir

COPY ./ /app

WORKDIR /app

RUN python3 manage.py migrate

RUN python3 manage.py fill_database_with_test_data

CMD ["python3", "manage.py", "runserver", "0:8000"]
