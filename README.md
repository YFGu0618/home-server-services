# Home Server Services

Home server services with Docker Compose, compiled from sources.

- [Home Server Services](#home-server-services)
  - [Tested Environment](#tested-environment)
  - [General Usage](#general-usage)
    - [1. Setup Environment Variables](#1-setup-environment-variables)
    - [2. Automatically start on boot](#2-automatically-start-on-boot)
    - [3. Start all services](#3-start-all-services)
    - [4. Stop all services](#4-stop-all-services)
    - [5. Debug with container logs](#5-debug-with-container-logs)
    - [6. Check resources usage](#6-check-resources-usage)
  - [Services Setup](#services-setup)
    - [1. Shadowsocks](#1-shadowsocks)
    - [2. Syncthing](#2-syncthing)
    - [3. RTorrent + Flood](#3-rtorrent--flood)
    - [4. Jellyfin](#4-jellyfin)

## Tested Environment

- Host OS: `Fedora 34 (Workstation Edition)`
- Host CPU: `Intel(R) Core(TM) i3-7100 CPU @ 3.90GHz`
- Docker Version: `Docker version 20.10.12, build e91ed57`
- Docker Compose Version: `docker-compose version 1.28.6, build unknown`

## General Usage

### 1. Setup Environment Variables

```shell
# Update .env file
sed -i "s|HOSTNAME=.*|HOSTNAME=$HOSTNAME|g; s|USERNAME=.*|USERNAME=$USERNAME|g" .env
```

### 2. Automatically start on boot

```shell
# Update home-servers.service file
SERVICE_DIR=$(realpath ./) sed -i "s|Environment=SERVICE_DIR=.*|Environment=SERVICE_DIR=$SERVICE_DIR|g; s|WorkingDirectory=.*|WorkingDirectory=$SERVICE_DIR|g; s|User=.*|User=$USERNAME|g" home-server.service

sudo cp home-server.service /etc/systemd/system/home-server.service
sudo systemctl enable home-server.service
```

### 3. Start all services

```shell
docker-compose up --build --remove-orphans -d
```

### 4. Stop all services

```shell
docker-compose down -v --remove-orphans
```

### 5. Debug with container logs

```shell
docker-compose logs -f [service_name]
```

### 6. Check resources usage

```shell
docker stats
```

## Services Setup

### 1. Shadowsocks

> [Shadowsocks](https://github.com/shadowsocks) is a fast tunnel proxy that helps you bypass firewalls. This service uses source code from [shadowsocks/shadowsocks-rust](https://github.com/shadowsocks/shadowsocks-rust).

- Update `shadowsocks/shadowsocks.json.example` file and copy it to `~/.config/shadowsocks.json`, which would be used by `ssserver` in `shadowsocks` service container as it's config.
- Shadowsocks service is accessible via `host_ip:8388` (default).

### 2. Syncthing

> [Syncthing](https://github.com/syncthing) is a continuous file synchronization program. This service uses source code from [syncthing/syncthing](https://github.com/syncthing/syncthing).

- Create the directory `mkdir -p ~/.config/syncthing`, which would be used for storing configs and other data used by the program.
- Syncthing Web GUI is accessible via `host_ip:8384` (default).

- More details see [Syncthing Documentation](https://docs.syncthing.net/index.html).

### 3. RTorrent + Flood

> [RTorrent](https://github.com/rakshasa/rtorrent) is a BitTorrent client. This service uses source code from [rakshasa/rtorrent](https://github.com/rakshasa/rtorrent).
>
> [Flood](https://github.com/jesec/flood) is a monitoring service for various torrent clients. This service uses source code from [jesec/flood](https://github.com/jesec/flood).

- Create the directory `mkdir -p  ~/.config/rtorrent`, which would be used for storing configs and other data by the program.
- Update `rtorrent/rtorrent.rc.example` file and copy it to `~/.config/rtorrent/rtorrent.rc`.
- Flood Web GUI is accessible via `host_ip:3000` (default).


### 4. Jellyfin

> [Jellyfin](https://jellyfin.org) is a Free Software Media System. This service uses Docker Hub image [jellyfin/jellyfin](https://hub.docker.com/r/jellyfin/jellyfin/).

- Create the directories `mkdir -p ~/.config/jellyfin/{config,cache}`, which would be used for storing configs and cache used by the program.
- Update `docker-compose.yaml` to configure [hardware acceleration](https://jellyfin.org/docs/general/administration/hardware-acceleration.html) accordingly.
- Jellyfin Web GUI is accessible via `host_ip:8096` (http) and/or `host_ip:8920` (https, if configured).
