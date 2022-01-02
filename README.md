# Home Server Services

Home server services with Docker Compose, compiled from sources.

- [Home Server Services](#home-server-services)
  - [General Usage](#general-usage)
    - [Start all services](#start-all-services)
    - [Stop all services](#stop-all-services)
    - [Check resources usage](#check-resources-usage)
  - [Services Setup](#services-setup)
    - [1. Shadowsocks](#1-shadowsocks)
    - [2. Syncthing](#2-syncthing)
    - [3. RTorrent + Flood](#3-rtorrent--flood)
    - [4. Jellyfin](#4-jellyfin)

## General Usage

### Start all services

```shell
docker-compose up --build --remove-orphans -d
```

### Stop all services

```shell
docker-compose down -v --remove-orphans
```

### Check resources usage

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
