FROM golang:1.17-bullseye as builder
ENV SYNCTHING_VERSION="v1.18.5"
RUN apt-get -qq update && \
    apt-get install -y -qq \
        git
WORKDIR /root/
RUN git clone https://github.com/syncthing/syncthing.git && \
    cd syncthing && \
    git checkout tags/"${SYNCTHING_VERSION}" -b build && \
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
ENTRYPOINT ["/home/syncthing/bin/syncthing"]
