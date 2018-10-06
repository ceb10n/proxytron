import requests
from bs4 import BeautifulSoup

import os

proxies = []

page = requests.get('https://free-proxy-list.net/')
soup = BeautifulSoup(page.text, 'html.parser')
table = soup.find('table', attrs={'id':'proxylisttable'})
body = table.find('tbody')

for row in body.find_all('tr'):
    cols = row.find_all('td')[:7]
    proxies.append({
        'ip': cols[0].text,
        'port': cols[1].text,
        'iso': cols[2].text,
        'country': cols[3].text,
        'protocol': 'https' if cols[6].text == 'yes' else 'http',
        'alive': True})

with open("proxies.txt","w+") as file:
    [file.write(f"{p['ip']}:{p['port']}\n") for p in proxies]

os.startfile('proxies.txt')
