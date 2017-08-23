from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen("http://en.wikipedia.org/wiki/Kevin_Bacon")
bsObj = BeautifulSoup(html)
for link in bsObj.find('div',{'id':'bodyContent'}).findAll('a',{'href':re.compile(r'^(/wiki)((?!:).)*$')}): #((?!:).)*表示不包括冒号的情况下匹配任意个单字符（符号数字空格字母）
    if 'href' in link.attrs:
        print(link.attrs['href'])