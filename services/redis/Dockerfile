FROM redis:6-bullseye
RUN apt-get -qq update && \
    apt-get install -y -qq \
        netcat && \
    rm -rf /var/lib/apt/lists/*
RUN groupadd -g 1000 redis_user && \
    useradd -g 1000 -m -s /usr/sbin/nologin -u 1000 redis_user
USER redis_user
WORKDIR /home/redis_user
COPY redis.conf /home/redis_user/redis.conf
ENTRYPOINT ["redis-server", "/home/redis_user/redis.conf"]
HEALTHCHECK --interval=30s --timeout=3s --start-period=10s \
  CMD nc -z 127.0.0.1 6379 || exit 1
