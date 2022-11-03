#!/bin/sh

echo "Waiting for db..."


while ! nc -z db 5432; do
  sleep 0.1
done

echo "DB started"

uvicorn app.main:app --host=0.0.0.0 --port=5000 --reload