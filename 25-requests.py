import requests

'''Requests 库:一个擅长处理那些复杂的HTTP 请求、cookie、header（响应头和请求头）等内容的Python 第三方库。'''

#提交文字表单
params={'firstname':'Ryan','lastname':'Mitchell'} #params的key为表单input中的'name'属性
r=requests.post('http://pythonscraping.com/files/processing.php', data=params)
print(r.text) #表单被提交之后，程序应该会返回执行页面的源代码

#提交单选按钮复选框滚动条等
'''开发者工具，headers-form data'''

#提交文件和图像
files = {'uploadFile': open('../files/Python-logo.png', 'rb')} #rb
r = requests.post("http://pythonscraping.com/pages/processing2.php",files=files)
print(r.text)

'''
关注两件事：
• 你想提交数据的字段名称，在input中
• 表单的action 属性，也就是表单提交后网站会显示的页面,在form中

'''

#coockie登录凭据
params={'username':'Ryan','password':'password'}
r=requests.post("http://pythonscraping.com/pages/cookies/welcome.php", params) #1.post-传表单
print(r.cookies.get_dict())
r = requests.get("http://pythonscraping.com/pages/cookies/profile.php",cookies=r.cookies) #2.get-得cookies传cookies
print(r.text)

#不需要cookies可以用session，会话对象持续跟踪
session=requests.Session()
params = {'username': 'username', 'password': 'password'}
s = session.post("http://pythonscraping.com/pages/cookies/welcome.php", params)
print(s.cookies.get_dict())
s = session.get("http://pythonscraping.com/pages/cookies/profile.php")
print(s.text)

#不用cookies的网站用HTTP基本接入认证，少见，requests.auth模块处理

#表单反扒陷阱：蜜罐，隐含字段 hidden field
