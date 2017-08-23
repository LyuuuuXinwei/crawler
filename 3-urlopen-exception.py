from urllib.request import urlopen

try:
    html=urlopen("http://pythonscraping.com/pages/page1.html")
except HTTPerror as e:
    print(e)
if html is None:
    print('not found')
else: