FROM python:3.10.4-slim-bullseye
RUN apt-get -qq update && \
    apt-get install -y -qq \
        procps && \
    rm -rf /var/lib/apt/lists/*
RUN groupadd -g 1000 dyndns && \
    useradd -g 1000 -m -s /usr/sbin/nologin -u 1000 dyndns
USER dyndns
WORKDIR /home/dyndns
COPY requirements.txt requirements.txt
RUN pip install -U pip -r requirements.txt
COPY ./src /home/dyndns/src
ENTRYPOINT ["python", "/home/dyndns/src/run.py"]
HEALTHCHECK --interval=30s --timeout=3s --start-period=10s \
  CMD ps -aux | grep -v grep | grep python
