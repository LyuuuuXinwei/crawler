from urllib.request import urlopen
from io import StringIO
import csv

#txt
textPage = urlopen("http://www.pythonscraping.com/pages/warandpeace/chapter1-ru.txt")
print(str(textPage.read(), 'utf-8'))

#csv
data = urlopen("http://pythonscraping.com/files/MontyPythonAlbums.csv").read().decode('ascii', 'ignore') #bytes变为str
datafile=StringIO(data) #可以像处理本地csv一样处理
#1
csv_reader=csv.reader(datafile)
for row in csv_reader:
    print(row) #每行返回一个list
#2
csv_dict_reader=csv.DictReader(datafile)
print(csv_dict_reader.fieldnames)
for row in csv_dict_reader:
    print(row) #每行返回一个dict，key为csv表头

#pdf docx略