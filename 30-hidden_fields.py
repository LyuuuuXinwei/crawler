'''
用隐含字段阻止网络数据采集的方式主要有两种:
1.表单页面上的一个字段可以用服务器生成的随机变量表示。如果提交时这个值不在表单处理页面上，服务器就有理由认为这个提交不是从原始表单页面上提交的
解决：先采集表单所在页面上生成的随机变量，然后再提交到表单处理页面
2.“蜜罐”（honey pot）表单里包含一个具有普通名称的隐含字段（设置蜜罐圈套）
解决：通过CSS 设置成对用户不可见，style：display：None /type:hidden/class:custon hidden right:5000px(屏幕外)不填写隐藏字段
'''

from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement #is_displayed()

driver = webdriver.PhantomJS(executable_path=r'F:\phantomjs-2.1.1-windows\bin\phantomjs')
driver.get("http://pythonscraping.com/pages/itsatrap.html")

#链接不可见
links = driver.find_elements_by_tag_name('a')
for link in links:
    if not link.is_displayed():
        print('the link：%s is a trap' % link.get_attribute('href'))

#输入不可见
fields=driver.find_elements_by_tag_name('input')
for field in fields:
    if not field.is_displayed():
        print('do not input the value of %s' % field.get_attribute('name'))

#selenium中的查找属性用get_attribute(''),bs用.attrs['']