from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(html)
soup=bsObj.findAll(lambda tag:len(tag.attrs)==2) #必须标签为参数，返回布尔
print(soup)