# Home Server Services

Home server services with Docker Compose, compiled from sources.

- [Home Server Services](#home-server-services)
  - [General Usage](#general-usage)
    - [1. Set Environment Variables/Secrets](#1-set-environment-variablessecrets)
    - [2. Docker Compose](#2-docker-compose)
    - [3. Enabling IPV6 for bridge networks](#3-enabling-ipv6-for-bridge-networks)


## General Usage

### 1. Set Environment Variables/Secrets

Update variables in `.env` file accordingly.

### 2. Docker Compose

```shell
# Start all services
docker-compose up --build --remove-orphans -d

# Stop all services
docker-compose down -v --remove-orphans
```

### 3. Enabling IPV6 for bridge networks

> Reference: <https://forums.docker.com/t/solution-docker-ipv6-and-docker-compose-woes/97852>

- Update `/etc/docker/daemon.json` file to include following:

    ```json
    {
        "ipv6": true,
        "fixed-cidr-v6": "2001:db8:1::/64"
    }
    ```

- Create iptables rules:

  ```shell
  # For the default bridge, as defined above
  sudo ip6tables -t nat -A POSTROUTING -s 2001:db8:1::/64 ! -o docker0 -j MASQUERADE
  # For the custom bridge, as defined in docker-compose.yaml
  sudo ip6tables -t nat -A POSTROUTING -s 2001:db8:a::/64 ! -o docker0 -j MASQUERADE
  ```
