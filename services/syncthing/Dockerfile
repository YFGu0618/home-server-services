FROM golang:1.18-bullseye as builder
ENV SYNCTHING_VERSION="v1.20.3"
RUN apt-get -qq update && \
    apt-get install -y -qq \
        git
WORKDIR /root/
RUN git clone --depth 1 --branch "${SYNCTHING_VERSION}" \
        https://github.com/syncthing/syncthing.git && \
    cd syncthing && \
    go run build.go -no-upgrade

FROM debian:bullseye-slim
RUN apt-get -qq update && \
    apt-get install -y -qq \
        netcat && \
    rm -rf /var/lib/apt/lists/*
RUN groupadd -g 1000 syncthing && \
    useradd -g 1000 -m -s /usr/sbin/nologin -u 1000 syncthing
USER syncthing
COPY --from=builder /root/syncthing/bin/ /home/syncthing/bin/
ENTRYPOINT ["/home/syncthing/bin/syncthing", "--no-browser", "--no-upgrade", "--gui-address=0.0.0.0:8384"]
HEALTHCHECK --interval=5m --timeout=3s --start-period=10s \
  CMD nc -z 127.0.0.1 8384 || exit 1
