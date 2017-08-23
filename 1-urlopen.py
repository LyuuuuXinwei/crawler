from urllib.request import urlopen

html=urlopen("http://pythonscraping.com/pages/page1.html")
print(html.read(),'utf-8')

with urlopen("http://pythonscraping.com/pages/page1.html") as html:
    for line in html:
        print(line)