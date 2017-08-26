from selenium import webdriver
import time
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By

#以下两个模块构成了selenium的隐式等待
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


#用PhantomJS 库创建了一个新的Selenium WebDriver，根据安装位置指明PantomJS可执行文件的路径
driver=webdriver.PhantomJS(executable_path=r'F:\phantomjs-2.1.1-windows\bin\phantomjs')
driver.get("http://pythonscraping.com/pages/javascript/ajaxDemo.html")

#显式等待：固定时间等待动态载入，不然可能会出现JS加载不完依然返回JS加载前的页面
time.sleep(3)
print(driver.find_element_by_id('content').text) #可以像bs一样查找页面元素

#隐式等待：
try:
    element=WebDriverWait(driver,10).until(EC.presence_of_element_located(By.ID,'loadedButton'))
    '''
    expected_conditions：EC，元素被触发的期望条件，期望条件使用前需要用定位器（一种抽象的查询语言）指定等待的元素，用BY对象表示
    (EC.presence_of_element_located(By.ID,'loadedButton'))查找id是loadedButton的按钮
    定位器配合选择器driver.find_element(By.ID, "content").text
    By.XPath:是在XML 文档中导航和选择元素的查询语言
    WebDriverWait(driver,10)：如果后面的条件没有满足就会等待10秒，属于明确等待
    driver.implicitly_wait(1)模糊等待
    '''
finally:
    print(driver.find_element_by_id('content').text)

#如果还是想用BS解析:
pagesource=driver.page_source
bsobj=BeautifulSoup(pagesource)

driver.close()