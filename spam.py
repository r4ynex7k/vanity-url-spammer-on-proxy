import time
import threading
import requests
import os
from itertools import cycle
from user_agent import generate_user_agent
from datetime import datetime
from requests.adapters import HTTPAdapter
from raynex.cmdlog import Logger

def oku(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file]

proxies = cycle(oku("./proxies.txt"))
tkns = cycle(oku('./tkn.txt'))

urls = ["url1, url2, url3, url4"] 
sw = "1208202703797485588"

session = requests.Session()
session.mount("", HTTPAdapter(max_retries=1))

sonbu = None

def rs(tkn, v, proxy, sw):
    headers = {"Authorization": tkn, "User-Agent": generate_user_agent()}
    try:
        r = session.patch(f"https://canary.discord.com/api/v7/guilds/{sw}/vanity-url", json={"code": v}, headers=headers, proxies={"https": proxy}, timeout=3)
        if r.status_code == 200:
            Logger.succ += 1
            Logger.Print(f"URL ALINDI {v}")
        else:
            Logger.Print(f"URL BANLI {v}")
            Logger.checked += 1
    except Exception:
        Logger.proxyError += 1

def spam(v, proxy):
    r = session.get(f"https://canary.discord.com/api/v7/invites/{v}?with_counts=true&with_expiration=true", proxies={"https": proxy}, timeout=3)
    return r.status_code

def check():
    while True:
        try:
            if sonbu:
                break
            proxy = next(proxies)
            tkn = next(tkns)

            for url in urls:
                response = spam(url, proxy)
                if response == 404:
                    rs(tkn, url, proxy, sw)
                elif response == 200:
                    Logger.checked += 1
                    Logger.Print(f"{datetime.now().strftime('%H:%M:%S')} DENENİYOR {url}")
                elif response == 429:
                    Logger.proxyError += 1
                else:
                    Logger.checked += 1
                    Logger.Print(f"{datetime.now().strftime('%H:%M:%S')} DENENİYOR {url}")
        except Exception:
            Logger.proxyError += 1

def uptitle():
    st = time.perf_counter()
    while True:
        time.sleep(0.1)
        duration = round(time.perf_counter() - st, 1)

if __name__ == "__main__":
    thread = threading.Thread(target=uptitle)
    thread.start()

    kingdom7k = [threading.Thread(target=check) for i in range(10000)]
    for thread in kingdom7k:
        thread.start()
