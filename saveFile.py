from bs4 import BeautifulSoup
import requests

proxies = {'http':'http://192.168.1.19:80'}

page = requests.get("http://magic.wizards.com/en/articles/archive/making-magic/mechanical-color-pie-2017-2017-06-05", proxies=proxies)

with open('maro', 'w') as maro:
    maro.write(page.text)