import re
import requests
from random import sample as randomsample
from urllib import request, response, error, parse
from urllib.request import urlopen
from bs4 import BeautifulSoup

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

def associated_press():
    url = 'https://apnews.com/'
    articlePattern = re.compile('/article')
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.content, features='html.parser')
    links = set()
    for section in soup.findAll('a'):
        link = str(section.get('href'))
        if articlePattern.match(link):
            links.add(link)
    output = [re.sub('^','https://apnews.com', link) for link in randomsample(links,10)]
    return output
