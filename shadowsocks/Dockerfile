FROM rust:1.57-slim-bullseye as builder
ENV SHADOWSOCKS_VERSION="v1.12.5"
ENV RUSTFLAGS="-C target-cpu=native"
RUN apt-get -qq update \
    && apt-get install -y -qq \
        build-essential \
        git
RUN rustup install nightly
WORKDIR /root/
RUN git clone --depth 1 --branch "${SHADOWSOCKS_VERSION}" \
        https://github.com/shadowsocks/shadowsocks-rust.git && \
    cd shadowsocks-rust && \
    cargo +nightly build --release

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
