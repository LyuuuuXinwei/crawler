import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup

'''HTML table存入CSV'''
html = urlopen("http://en.wikipedia.org/wiki/Comparison_of_text_editors")
bsObj = BeautifulSoup(html)
table=bsObj.findAll('table',{'class':'wikitable'})[0]
rows=table.findAll('tr')

csv_file=open(r'C:\Python\crawler\csv\test.csv','wt',newline='',encoding='utf-8') #文件对象
writer=csv.writer(csv_file) #创建写入对象

try:
    for row in rows:
        csv_row = []
        for cell in row.findAll(['th','td']):
            csv_row.append(cell.get_text()) #把HTML table的每一行写入一个list
        writer.writerow(csv_row) #把list writerow进'写入对象',不能file.writerow
finally:
    csv_file.close() #似乎可以用with open

