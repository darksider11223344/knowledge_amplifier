FROM python:3.9-alpine

RUN mkdir -p /app

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

CMD ["faust", "-A", "consumer", "worker", "-l", "info"]