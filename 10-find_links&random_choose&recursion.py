from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import datetime
import random

random seed(datetime.datetime.now()) #随机数种子
def get_links(url):
    html = urlopen(url)
    bsObj = BeautifulSoup(html)
    link_lists=bsObj.find('div',{'id':'bodyContent'}).findAll('a',{'href':re.compile(r'^(/wiki)((?!:).)*$')})
    return link_lists

links=get_links("http://en.wikipedia.org/wiki/Kevin_Bacon"):
while len(links)>0:
    newurl=links[random.randint(0,len(links)-1)].attrs['href'] # random choose new url
    print('jump to URL:%s'% newurl)
    links=get_links(newurl)
