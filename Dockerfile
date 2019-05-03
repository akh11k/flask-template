FROM ubuntu:18.04

WORKDIR /app

RUN apt-get update && \
    apt-get install -y \
    python3.6 \
    python3-pip \
    supervisor && \
    rm -rf /var/lib/apt/lists/*

COPY requirements.txt requirements.txt

RUN python3 -m pip install -r requirements.txt && rm -rf /root/.cache

RUN python3 -m pip install j2cli

COPY src src
COPY conf conf
COPY entry-point.sh ./

RUN chmod +x ./entry-point.sh

ENV PYTHONPATH $PYTHONPATH:/app/src
ENV FLASK_APP /app/src/factory.py
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

EXPOSE 8080
ENTRYPOINT ["./entry-point.sh"]
