import re
import string


'''下面的代码将返回维基百科词条“Python programming language”的2-gram 列表,并统计词频'''
'''
清洗步骤：
1.不清洗，发现杂点
2.制定清洗任务，如：剔除转义字符，单字符单词，维基百科引用符号，标点号，大小写统一
3.转变为代码,常用字符串方法如split，strip，转码，re,string模块等
'''
def clean(input):
    #先清洗处理的数据
    #处理转义字符\n
    input=re.sub('\n+',' ',input)
    input=re.sub(' +',' ',input)
    #过滤Unicode字符
    input=bytes(input,'utf-8') # str变为bytes
    input=input.decode('ascii','ignore') # bytes按ascii解码回str
    #转为2grams
    input=input.split(' ')
    cleaninput=[]
    for item in input:
        item=item.strip(string.punctuation) #去掉標點，strip移除字符串頭尾指定的字符
        if len(item)>1 or (item.lower()=='i'or'a'):
            cleaninput.append(item)
    return cleaninput #单层list

