from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import datetime
import random

'''学着用函数将单一作用的代码模块分离，再用单一函数构建作用复合的高阶函数，操作集'''

pages={}
random.seed(datetime.datetime.now())

def get_internal_links(bsobj,include_url):
    internal_links=[]
    for link in bsobj.findAll('a',href=re.compile('^(/|.*'+include_url+')')):
        if 'href' in bsobj.attrs:
            if bsobj.attrs['href'] not in internal_links:
                internal_links.append(bsobj.attrs['href'])
    return internal_links

def get_external_links(bsobj,exclude_url):
    external_links=[]
    for link in bsobj.findAll('a',href=re.compile('^(http|www)((?!'+exclude_url+').)*$')):
        if 'href' in bsobj.attrs:
            if bsobj.attrs['href'] not in external_links:
                external_links.append(bsobj.attrs['href'])
    return external_links

def split_address(address):
    ad=address.replace('http://','').split('/')
    return ad

def get_random_external_link(start_page):
    html=urlopen(start_page)
    bsobj=BeautifulSoup(html)
    external_links=get_external_links(bsobj,split_address(start_page)[0])
    if len(external_links)==0:
        internal_links=get_internal_links(bsobj,split_address(start_page))
        return internal_links[random.randint(0,len(internal_links)-1)]
    else:
        return external_links[random.randint(0,len(external_links)-1)]

def follow_external_only(start_site):
    i=0
    while 1<50:
        external_link=get_random_external_link(start_site)
        print('随即外链为：'+external_link)
        i+=1
        follow_external_only(external_link)

follow_external_only('http://oreilly.com')