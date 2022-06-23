FROM python:3.8-slim

EXPOSE 5000/tcp

WORKDIR /app

COPY . .

RUN apt-get update \
    && apt-get install --yes --no-install-recommends \
        gcc g++ libffi-dev 


RUN pip install -r requirements.txt

COPY app.py .

CMD [ "flask", "run", "--host", "0.0.0.0"]