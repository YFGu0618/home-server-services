#!/usr/bin/env python3

import json
import logging
import os
import time

import requests

INTERVAL = os.environ["INTERVAL"]
IP_HISTORY = os.environ["IP_HISTORY"]
DYNDNS_SECRETS = os.environ["DYNDNS_SECRETS"]
HEADERS = {
    "Authorization": "Basic base64-encoded-auth-string",
    "User-Agent": "dyndns-client/0.1 yfgu0618@outlook.com",
}


def get_public_ip():
    ip = requests.get("https://api.ipify.org").text
    return ip


# https://support.google.com/domains/answer/6147083
def update_google_dns():
    with open(IP_HISTORY, "r", encoding="utf-8") as f:
        last_ts, last_ip = f.readlines()[-1].split("|")
    current_ip = get_public_ip()

    if current_ip == last_ip:
        logging.info("Public IP hasn't changed.")
    else:
        with open(IP_HISTORY, "a", encoding="utf-8") as f:
            f.write(f"\n{time.time()}|{current_ip}")
        logging.info("Public IP changed, start updating DynDNS...")

        with open(DYNDNS_SECRETS, "r", encoding="utf-8") as f:
            secrets = json.load(f)
            for hostname, basic_auth in secrets.items():
                url = f"https://{basic_auth}@domains.google.com/nic/update"
                params = {"hostname": hostname, "myip": current_ip}
                r = requests.post(url, headers=HEADERS, params=params).text
                if r in [f"good {current_ip}", f"nochg {current_ip}"]:
                    logging.info(f"Successfully updated DynDNS: {hostname}")
                else:
                    logging.error(f"Failed updating DynDNS: {hostname}")
                    raise RuntimeError(r)


def main():
    while True:
        update_google_dns()
        time.sleep(int(INTERVAL))


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s;%(threadName)s;%(levelname)s - %(message)s",
    )
    main()
