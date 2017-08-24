from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

links={}
def get_links(pageUrl):
    '''递归获取维基百科某页面词条所有直接间接链接的标题和第一段文字'''
    global links
    html=urlopen("http://en.wikipedia.org"+pageUrl)
    bsobj=BeautifulSoup(html)
    try:
        print(bsobj.h1.get_text()) #获取标题
        print(bsobj.find(id='mw-content-text').findAll('p')[0]) #获取第一段正文文字
    except AttributeError as e:
        print('缺少属性')

    link_lists = bsObj.find('div', {'id': 'bodyContent'}).findAll('a', {'href': re.compile(r'^(/wiki)((?!:).)*$')})
    while link_lists>0:
        for link in link_lists:
            if 'href' in link.attrs:
                if link.attrs['href'] not in links:
                    newlink=link.attrs['href']
                    print(newlink)
                    links.add(newlink)
                    get_links(newlink)

get_links('')