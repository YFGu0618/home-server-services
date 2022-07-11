FROM debian:bullseye
RUN dpkg --add-architecture i386 && \
    apt-get -qq update && \
    apt-get -qq install -y \
        curl \
        wget \
        file \
        tar \
        bzip2 \
        gzip \
        unzip \
        bsdmainutils \
        python3 \
        util-linux \
        ca-certificates \
        binutils \
        bc \
        jq \
        tmux \
        netcat \
        lib32gcc-s1 \
        lib32stdc++6 \
        cpio \
        cron \
        distro-info \
        iproute2 \
        libc6-dev \
        libsdl2-2.0-0:i386 \
        locales \
        procps \
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
RUN wget -qO linuxgsm.sh https://linuxgsm.sh && \
    chmod +x linuxgsm.sh && \
    bash linuxgsm.sh vhserver && \
    ./vhserver auto-install && \
    echo "valheimplus" | ./vhserver mods-install
RUN (crontab -l 2>/dev/null; echo "0 4 * * * /home/vhserver/vhserver backup") | crontab -
COPY entrypoint.sh entrypoint.sh
ENTRYPOINT ["bash", "entrypoint.sh"]
