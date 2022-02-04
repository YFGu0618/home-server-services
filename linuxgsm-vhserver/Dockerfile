FROM debian:bullseye-slim as builder
RUN dpkg --add-architecture i386 && \
    apt-get -qq update && \
    apt-get -qq install -y \
        apt-utils \
        bc \
        binutils \
        bsdmainutils \
        bzip2 \
        ca-certificates \
        cpio \
        cron \
        curl \
        debconf-utils \
        file \
        gzip \
        iproute2 \
        jq \
        lib32gcc-s1 \
        lib32stdc++6 \
        libc6-dev \
        libsdl2-2.0-0:i386 \
        locales \
        netcat \
        procps \
        python3 \
        tar \
        tmux \
        unzip \
        util-linux \
        wget \
        xz-utils && \
    rm -rf /var/lib/apt/lists/* && \
    localedef -i en_US -c -f UTF-8 -A /usr/share/locale/locale.alias en_US.UTF-8
RUN groupadd -g 1000 vhserver && \
    useradd -g 1000 -m -u 1000 vhserver
USER vhserver
WORKDIR /home/vhserver
RUN mkdir -p bin && \
    curl -sqL "https://steamcdn-a.akamaihd.net/client/installer/steamcmd_linux.tar.gz" \
        | tar zxf - -C bin && \
    mv bin/steamcmd.sh bin/steamcmd && \
    chmod +x bin/steamcmd
ENV PATH="${HOME}/bin:${PATH}"
RUN wget -O linuxgsm.sh https://linuxgsm.sh && \
    chmod +x linuxgsm.sh && \
    ./linuxgsm.sh vhserver && \
    ./vhserver auto-install
RUN (crontab -l 2>/dev/null; echo "0 4 * * * /home/vhserver/vhserver backup") | crontab -
COPY entrypoint.sh entrypoint.sh
ENTRYPOINT ["bash", "entrypoint.sh"]
