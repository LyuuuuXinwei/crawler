import json
from urllib.request import urlopen

def getCountry(ip):
    dictata=urlopen("http://freegeoip.net/json/"+ip).read().decode('utf-8') #read返回二进制数据,解码
    json_data=json.loads(data) #反序列化：json(str)变为dict
    return json_data.get('country_code')

print(getCountry("50.78.253.58"))
