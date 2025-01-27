FROM python:3.12.6-alpine

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt --no-cache-dir

COPY . /app

EXPOSE 1404

CMD sh -c /app/start.sh