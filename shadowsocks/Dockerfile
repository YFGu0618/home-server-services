FROM rust:1.59-slim-bullseye as builder
ENV SHADOWSOCKS_VERSION="v1.14.3"
ENV RUSTFLAGS="-C target-cpu=native"
RUN apt-get -qq update \
    && apt-get install -y -qq \
        build-essential \
        git
WORKDIR /root/
RUN git clone --depth 1 --branch "${SHADOWSOCKS_VERSION}" \
        https://github.com/shadowsocks/shadowsocks-rust.git && \
    cd shadowsocks-rust && \
    cargo build --release

FROM debian:bullseye-slim
RUN apt-get -qq update && \
    apt-get install -y -qq \
        netcat && \
    rm -rf /var/lib/apt/lists/*
RUN groupadd -g 1000 shadowsocks && \
    useradd -g 1000 -m -s /usr/sbin/nologin -u 1000 shadowsocks
USER shadowsocks
COPY --from=builder /root/shadowsocks-rust/target/release/ss* /home/shadowsocks/bin/
ENTRYPOINT ["/home/shadowsocks/bin/ssserver", "-c", "/home/shadowsocks/.config/shadowsocks.json"]
HEALTHCHECK --interval=30s --timeout=3s --start-period=10s \
  CMD nc -z 127.0.0.1 8388 || exit 1
