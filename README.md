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

> [Shadowsocks](https://github.com/shadowsocks) is a fast tunnel proxy that helps you bypass firewalls. This service uses [shadowsocks-rust](https://github.com/shadowsocks/shadowsocks-rust).

Update `shadowsocks/shadowsocks.json.example` file and copy it to `${HOME}/.config/shadowsocks.json`, which would be used by `ssserver` in `shadowsocks` service container as it's config.

### 2. Syncthing

> [Syncthing](https://github.com/syncthing) is a continuous file synchronization program. This service uses [syncthing](https://github.com/syncthing/syncthing).

Create the directory `${HOME}/.config/syncthing`, which would be used by Syncthing to store configs and other data used by the program.

The Web GUI is default to only accessible locally, if plan to access from external devices, update `address` in `${HOME}/.config/syncthing/config.xml`:

```xml
<address>0.0.0.0:8384</address>
```

More details see [Syncthing Documentation](https://docs.syncthing.net/index.html).
