#!/bin/bash

# First, we need to deploy SQL in backend.
# To Deploy PostgreSQL on Kubernetes we need to follow below steps:
# 1, prepare secrets used by k8s
kubectl create -f ./k8s/postgres-secrets.yaml

# 2, prepare persistant storage volume used by postgres db
kubectl create -f ./k8s/postgres-storage.yaml

# 3, deploy postgres db from docker image
kubectl create -f ./k8s/postgres-deployment.yaml


# Second, we need to build a local docker image for flask app
# 1, build a local image
docker build --tag flask-app:latest .

# 2, deploy flask app from above image
kubectl create -f ./k8s/flask-deployment.yaml

sleep 15

# Then, import date to SQL db
# 1, copy csv file into docker container
docker cp titanic.csv `docker ps -aqf "name=postgres_postgres"`:/var/lib/postgresql/data/titanic.csv
docker cp csv2db.txt `docker ps -aqf "name=postgres_postgres"`:/var/lib/postgresql/data/csv2db.txt

# 2, import csv to db by using psql commands
docker exec -it `docker ps -aqf "name=postgres_postgres"` psql -U postgresadmin -d postgresdb -f /var/lib/postgresql/data/csv2db.txt

echo "Now you can browse the url via http://localhost:"`kubectl get svc -l app=flask -o wide | grep -v PORT | awk -F':' '{print $2}' | awk -F'/' '{print $1}'`





