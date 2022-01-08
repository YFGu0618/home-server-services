FROM node:lts-bullseye-slim as builder
ENV FLOOD_VERSION="v4.7.0"
RUN apt-get -qq update && \
    apt-get install -y -qq \
        git
WORKDIR /root/
RUN git clone https://github.com/jesec/flood.git && \
    cd flood && \
    git checkout tags/"${FLOOD_VERSION}" -b build && \
    npm install && \
    npm run build && \
    rm -rf node_modules && \
    npm install --production

FROM debian:bullseye-slim
RUN apt-get -qq update && \
    apt-get install -y -qq \
        netcat \
        nodejs && \
    rm -rf /var/lib/apt/lists/*
RUN groupadd -g 1000 rtorrent && \
    useradd -g 1000 -m -s /usr/sbin/nologin -u 1000 rtorrent
USER rtorrent
COPY --from=builder /root/flood/dist/ /home/rtorrent/
COPY --from=builder /root/flood/node_modules/ /home/rtorrent/node_modules/
ENTRYPOINT ["/usr/bin/node", "/home/rtorrent/index.js", "--host", "0.0.0.0", "--port", "3000", "--auth", "default", "--rundir", "/home/rtorrent/rtorrent/flood", "--allowedpath", "/home/rtorrent/torrent"]
