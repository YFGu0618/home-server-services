FROM debian:bullseye-slim as builder
ENV BUILD_DIR="/root/build"
ENV PATH="${BUILD_DIR}/bin:${PATH}"
ENV LD_LIBRARY_PATH="${BUILD_DIR}/lib/:${LD_LIBRARY_PATH}"
ENV PKG_CONFIG_PATH="${BUILD_DIR}/lib/pkgconfig:${PKG_CONFIG_PATH}"
ENV XMLRPC_VERSION="1.58.04"
ENV LIBTORRENT_VERSION="v0.13.8"
ENV RTORRENT_VERSION="v0.9.8"
RUN apt-get -qq update && \
    apt-get install -y -qq \
        automake \
        build-essential \
        git \
        pkg-config \
        libtool \
        subversion \
        libcurl4-openssl-dev \
        libcppunit-dev \
        libcrypto++-dev \
        libncurses5-dev \
        libncursesw5-dev \
        libssl-dev \
        zlib1g-dev
WORKDIR /root/
RUN svn checkout "http://svn.code.sf.net/p/xmlrpc-c/code/release_number/${XMLRPC_VERSION}" xmlrpc-c && \
    cd xmlrpc-c && \
    ./configure --prefix="${BUILD_DIR}" --with-libwww-ssl && \
    make -j$(nproc) && \
    make install
RUN git clone --depth 1 --branch "${LIBTORRENT_VERSION}" \
        https://github.com/rakshasa/libtorrent.git && \
    cd libtorrent && \
    ./autogen.sh && \
    ./configure --prefix="${BUILD_DIR}" --with-zlib && \
    make -j$(nproc) && \
    make install
RUN git clone  --depth 1 --branch "${RTORRENT_VERSION}" \
        https://github.com/rakshasa/rtorrent.git && \
    cd rtorrent && \
    ./autogen.sh && \
    ./configure --prefix="${BUILD_DIR}" \
        --enable-ipv6 \
        --with-ncurses \
        --with-libcurl \
        --with-xmlrpc-c && \
    make -j$(nproc) && \
    make install

FROM debian:bullseye-slim
RUN apt-get -qq update && \
    apt-get install -y -qq \
        libcppunit-1.15-0 \
        libcurl4 \
        libncursesw6 \
        netcat && \
    rm -rf /var/lib/apt/lists/*
RUN groupadd -g 1000 rtorrent && \
    useradd -g 1000 -m -s /usr/sbin/nologin -u 1000 rtorrent
USER rtorrent
COPY --from=builder /root/build/lib/ /usr/lib/
COPY --from=builder /root/build/bin/ /usr/bin/
ENTRYPOINT ["/usr/bin/rtorrent", "-o", "import=/home/rtorrent/rtorrent.rc"]
