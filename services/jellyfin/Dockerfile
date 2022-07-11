FROM jellyfin/jellyfin:10.8.1
RUN apt-get -qq update \
    && apt-get install -y -qq \
        fonts-noto \
    && rm -rf /var/lib/apt/lists/*
RUN groupadd -g 1000 jellyfin && \
    useradd -g 1000 -m -s /usr/sbin/nologin -u 1000 jellyfin
USER jellyfin
ENTRYPOINT ["/jellyfin/jellyfin", "-c", "/home/jellyfin/.config", "-d", "/home/jellyfin/.config/data", "-C", "/home/jellyfin/.config/cache", "-l", "/home/jellyfin/.config/log"]
