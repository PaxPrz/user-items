FROM python:3.9-slim

WORKDIR /app

COPY . .

RUN apt update && \
    apt install -y libpq-dev python3-dev && \
    apt install -y gcc && \
    rm -rf /var/cache/apt/archives/*
RUN pip install --no-cache poetry && \
    poetry config virtualenvs.create false && \
    poetry install --no-dev && \
    pip cache purge

CMD ["python", "cli.py", "serve"]
