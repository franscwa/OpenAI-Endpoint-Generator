FROM python:3.9-alpine

EXPOSE 5000/tcp

WORKDIR /app

COPY requirements.txt .

RUN pip install -r "requirements.txt"

COPY app.py .

