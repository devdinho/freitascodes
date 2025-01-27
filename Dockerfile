FROM python:3.12.6-slim

RUN useradd -ms /bin/bash devdinho

USER devdinho

WORKDIR /app

RUN chown -R devdinho /app

COPY --chown=devdinho:devdinho . /app

RUN chmod +x /app/start.sh

RUN pip install -r requirements.txt --no-cache-dir

CMD sh -c /app/start.sh