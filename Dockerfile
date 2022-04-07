# syntax=docker/dockerfile:1

FROM python:3.10

WORKDIR /flask

RUN python3 -m pip install --upgrade pip

RUN pip3 install virtualenv

RUN python3 -m virtualenv /venv

ENV PATH="/venv/bin:$PATH"

COPY ./python/flask/ .

RUN pip3 install -r requirements.txt

ENV DATABASE_URL=postgresql+psycopg2://postgresadmin:admin123@postgres:5432/postgresdb

EXPOSE 5000

CMD ["python3", "run.py"]
