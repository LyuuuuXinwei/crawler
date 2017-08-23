from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

html=urlopen("http://www.pythonscraping.com/pages/page1.html")
bsobj=BeautifulSoup(html.read())
try:
    data=bsobj.tag
except AttributeError as e:
else:
    if data==None:
    else:

def gettitle(url):
    try:
        html=urlopen(url)
    except HTTPError as e:
        return None
    try:
        bsobj=BeautifulSoup(html)
        title=bsobj.h1
    except AttributeError as e:
        return None
    return title

title=gettitle("http://www.pythonscraping.com/pages/page1.html")
if title=None:
    print('can not find title')
else:
    print(title)