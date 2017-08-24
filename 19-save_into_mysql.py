from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import datetime
import random
import pymysql

conn=pymysql.connect(host='localhost',port=3306,user='root',passwd='2981826123',db='scraping',charset='utf8')
cur=conn.cursor()
cur.execute('USE scraping')

random.seed(datetime.datetime.now())

def store(title,content):
    cur.execute('INSERT INTO pages (title,content) VALUES (\'%s\',\'%s\')',(title,content)) #占位符用法
    cur,connection.commit()# commit

def getlinks(url):
    html = urlopen("http://en.wikipedia.org"+url)
    bsObj = BeautifulSoup(html)
    title=bsObj.find('h1'),get_text()
    content=bsObj.find('div',{'id':'mw-content-text'}).find('p').get_text()
    store(title,content)
    return bsObj.find("div", {"id":"bodyContent"}).findAll("a",href=re.compile("^(/wiki/)((?!:).)*$"))

links=getlinks('/wiki//Kevin_Bacon')
try:
    while len(links)>0:
        newurl=links[random.randint(0,len(links)-1)].attrs['href']
        print(newurl)
        links=getlinks(newurl)
finally:
    cur.close()
    conn.close()
