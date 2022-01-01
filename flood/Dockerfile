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

FROM node:lts-bullseye-slim
RUN apt-get -qq update && \
    apt-get install -y -qq \
        netcat && \
    rm -rf /var/lib/apt/lists/*
COPY --from=builder /root/flood/dist/ /home/node/
COPY --from=builder /root/flood/node_modules/ /home/node/node_modules/
ENTRYPOINT ["/usr/local/bin/node", "/home/node/index.js", "--host", "0.0.0.0", "--port", "3000", "--allowedpath", "/home/flood/torrent"]
