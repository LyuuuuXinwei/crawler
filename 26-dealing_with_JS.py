'''
常用JS库：
1.jQuery
动态生成HTML
一个网站使用jQuery 的特征，就是源代码里包含了jQuery 入口：
<script src="http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js"></script>
2. Google Analytics
判断一个页面是不是使用了Google Analytics，底部：
<!-- Google Analytics -->
<script type="text/javascript">

ajax和DHTML：
如果提交表单之后，你访问的网站就在用Ajax 技术，全称是Asynchronous JavaScript and XML（异步JavaScript 和XML）
网站不需要使用单独的页面请求就可以和网络服务器进行交互（收发信息）
DHTML 是用客户端语言改变页面的HTML 元素（HTML、CSS，或者二者皆被改变）。比如，页面上的按钮只有当用户移动鼠标之后才出现，背景色可能每次点击都会改变

用Python爬Ajax 或DHTML 技术改变/ 加载内容的页面只有两种途径：
1.直接从JavaScript 代码里采集内容
2.用Python 的第三方库运行JavaScript，直接采集你在浏览器里看到的页面
2的代表是selenium（让浏览器自动加载界面）+phantomJS（无头浏览器，加载JS不向用户展示界面）
'''