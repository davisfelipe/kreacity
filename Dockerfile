FROM python:3.7.9-slim-buster
EXPOSE 8080

ENV PYTHONUNBUFFERED 1
ENV APP_HOME /app
ENV VENV /opt

WORKDIR ${VENV}

COPY requirements.txt .

RUN python -m venv .venv \
    && . .venv/bin/activate \
    && pip install --no-cache-dir -U pip \
    && pip install --no-cache-dir -r requirements.txt

WORKDIR ${APP_HOME}

COPY src src
COPY main.py .
COPY docker-entrypoint.sh .

ENTRYPOINT ["/bin/bash"]

CMD ["./docker-entrypoint.sh"]
