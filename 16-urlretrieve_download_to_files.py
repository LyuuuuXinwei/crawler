from urllib.request import urlretrieve
from urllib.request import urlopen
from bs4 import BeautifulSoup
import os

#下载单张图
html = urlopen("http://www.pythonscraping.com")
bsObj = BeautifulSoup(html)
image_location=bsObj.find('a',{'id':'logo'}).findAll('img')['src']
urlretrieve(image_location,'logo.jpg')

#批量
base_url="http://pythonscraping.com"
download_directory='download'

def get_absolute_url(base_url,source):
    '''url可以用startwith方法规范'''
    if source.startwith('http://www.'):
        url='http://'+source[11:]
    elif source.startwith('http://'):
        url=source
    elif source.startwith('www.'):
        url='http://'+source[4:]
    else:
        url=base_url+'/'+source
    if base_url not in url:
        return None #去掉外链
    return url

def get_download_path(base_url,absolute_url,download_directory):
    path=absolute_url.replace('www','')
    path=path.replace(base_url,'')
    path=download_directory+path
    directory=os,path.dirname(path) #根据文件返回路径

    if not os.path.exists(directory):
        os.mkdir(directory)
    return path

html=urlopen(base_url)
bsObj=BeautifulSoup(html)
download_lists=bsObj.findAll(src=True) #有src标签，lambda

for link in download_lists:
    file_url=get_absolute_url(base_url,link['src'])
    if file_url is not None:
        print(file_url)
    urlretrieve(file_url,get_download_path(base_url,file_url,download_directory))

'''<img src="https://cdn.oreillystatic.com/oreilly/home/assets/deeper01.jpg" alt="Training attendees">'''
'''代码缺少类型检查'''
