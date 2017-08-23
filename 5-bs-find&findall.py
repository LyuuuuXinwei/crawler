from urllib.request import urlopen
from bs4 import BeautifulSoup

html=urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
bsobj=BeautifulSoup(html)

find==finall(limit=1)

#根据属性和标签寻找
namelist=bsobj.findAll('span',{'class':{'green','red'}}) #寻找所有span标签
for name in namelist:
    print(name.get_text())
namelist=bsobj.span.findAll({'class':{'green','red'}}) #寻找第一个span标签

#根据属性寻找
namelist=bsobj.findAll(id='text') #'class'='green'
namelist=bsobj.findAll('',{'id':'text'})
bsobj.h1

#根据标签寻找
namelist=bsobj.findAll('h1')

#根据内容寻找text关键字
textlist=bsobj.findAll(text='the prince')
print(len(textlist))

#根据标签中的文字查找
navigablestring

#根据注释标签查找
comment

#根据标签在文档中的位置-标签嵌套的导航树
html2=urlopen("http://www.pythonscraping.com/pages/page3.html")
bsobj2=BeautifulSoup(html2)

for child in bsobj2.find('table',{'id':'giftList'}).children: #子标签
    print(child)
for d in bsobj2.find('table',{'id':'giftList'}).descendants: #后代标签
    print(d)
for br in bsobj2.find('table',{'id':'giftList'}).tr.next_siblings: #兄弟标签 previous_sibling
    print(br)
print(bsObj.find("img",{"src":"../img/gifts/img1.jpg"}).parent.previous_sibling.get_text()) #父标签




