from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen("http://www.pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(html)
images=bsObj.findAll('img',{'src':re.compile(r'../img/gifts/img[0-9]*.jpg')})
for img in images:
    print(img['src'])
#tag.attrs获取全部属性，tag[attr]