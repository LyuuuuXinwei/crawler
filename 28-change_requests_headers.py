'''
HTTP有大概十几种请求头

经典的Python 爬虫在使用urllib 标准库时，都会发送如下的请求头：
Accept-Encoding identity
User-Agent Python-urllib/3.4

大多数浏览器大概发的请求头：
Host https://www.google.com/
Connection keep-alive
Accept text/html，application/xhtml+xml，application/xml;q=0.9，image/webp，*/*;q=0.8
User-Agent Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.36 (KHTML, like
Gecko) Chrome/39.0.2171.95 Safari/537.36
Referrer https://www.google.com/
Accept-Encoding gzip，deflate，sdch
Accept-Language en-US,en;q=0.8
'''

from bs4 import BeautifulSoup
import requests

session=requests.Session()
headers={"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5)AppleWebKit 537.36 (KHTML, like Gecko) Chrome",
"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"}
#人造表头最重要的是user-agent，警觉性高的网站也会查别的，注意移动设备表头的巧妙使用，移动设备往往反扒做的没那么严格
url = "https://www.whatismybrowser.com/developers/what-http-headers-is-my-browser-sending"

#session.get可以传headers，session.post可以传表单
req=session.get(url,headers=headers)
bsObj=BeautifulSoup(req.text)
print(bsObj.find('table',{'class':'table-striped'}).get_text)