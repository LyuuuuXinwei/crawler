from selenium import webdriver

#用selenium的driver.get_cookies轻松获取动态cookies
driver=webdriver.PhantomJS(executable_path=r'F:\phantomjs-2.1.1-windows\bin\phantomjs')
driver.get("http://pythonscraping.com")
driver.implicitly_wait(1) #模糊等待，在一个范围内（0-1）
saved_cookies=driver.get_cookies() #获取cookies
print(saved_cookies)

driver2=webdriver.PhantomJS(executable_path=r'F:\phantomjs-2.1.1-windows\bin\phantomjs')
driver2.get("http://pythonscraping.com")
driver2.delete_all_cookies()

for cookie in saved_cookies:
    driver2.add_cookie(cookie) #用driver的cookies完全覆盖driver2

driver2.get("http://pythonscraping.com")
driver2.implicitly_wait(1)
print(driver2.get_cookies()) #此时将返回和driver相同的cookies