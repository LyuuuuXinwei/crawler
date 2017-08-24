'''
api请求使用严格的语法，用JSON,XML表示数据（格式友好）而非HTML--和URL访问的区别
部分API需要验证，令牌
API调用语法不尽相同，准则：
http://socialmediasite.com/users/1234/posts?from=08012014&to=08312014
http://socialmediasite.com/api/v4/json/users/1234/posts?from=08012014&to=08312014
http://socialmediasite.com/users/1234/posts?format=json&from=08012014&to=08312014
指定版本，数据格式和其他属性的位置：不指定/在文件路径/在请求参数

Echo Nest调用示例：
Monty Python 喜剧乐团：http://developer.echonest.com/api/v4/artist/search?api_key=<你的api_key>&name=monty%20python
歌曲id: http://developer.echonest.com/api/v4/artist/songs?api_key=<你的api_key>&id=AR5HF791187B9ABAF4&format=json&start=0&results=10
歌曲名： http://developer.echonest.com/api/v4/artist/songs?api_key=<你的api_key>2&name=monty%20python&format=json&start=0&results=10
'''

from twitter import Twitter

#Twitter 的验证系统用OAuth 验证，换成自己的OAuth,链接Twitter API
t=Twitter(auth=OAuth(<Access Token>,<Access Token Secret>,<Consumer Key>,<Consumer Secret>))

#打印包含#Python标签的推文JSON列表
python_tweets=t.search.tweets(q='#python')
print(python_tweets)

#发表推文
statusUpdate = t.statuses.update(status='Hello, world!')
print(statusUpdate)

'''
Google geocode API调用示例：
https://maps.googleapis.com/maps/api/geocode/json?address=1+Science+Park+Boston+MA+02114&key=<你的API key>
Google time zone API调用示例:
https://maps.googleapis.com/maps/api/timezone/json?location=42.3677994,-71.0708078&timestamp=1412649030&key=<你的 API key>

freegeoip.net API可以通过网站IP查询地理位置
调用示例：http://freegeoip.net/json/50.78.253.58
返回JSON：
{"ip":"50.78.253.58","country_code":"US","country_name":"美国","region_
code":"MA","region_name":"Massachusetts","city":"Chelmsford","zipcode":"01824",
"latitude":42.5879,"longitude":-71.3498,"metro_code":"506","area_code":"978"}
'''

