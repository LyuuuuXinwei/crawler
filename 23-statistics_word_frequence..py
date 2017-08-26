from urllib.request import urlopen
from bs4 import BeautifulSoup
from collections import OrderedDict
from collections import Counter
from 22-clean_data import clean
import operator

#方法1：把文本词段整理成2-grams列表并用Counter为列表进行统计排序
def ngrams(input,n):
    input=clean(input)
    output=[]
    for i in range(0, len(input)-n+1):
        output.append(input[i:i + n])  # 切片添加
    return output

html = urlopen("http://en.wikipedia.org/wiki/Python_(programming_language)")
bsObj = BeautifulSoup(html)
content = bsObj.find("div", {"id":"mw-content-text"}).get_text() #type：str
ngrams = ngrams(content, 2)
print(ngrams) #[['', 'Python'], ['Python', 'Paradigm'], ['Paradigm', 'multi-paradigm'], ['multi-paradigm', 'object-oriented'],

#看似可以的方法1
# d={str(x):x.count for x in ngrams}

#看似可以的方法2
# d={}
# for i in ngrams:
#     d[str(i)]=ngrams.count(i)
# print(d)
# unhashable type: 'list'

#真的可以的方法3
c=Counter(str(x) for x in ngrams) #str(x)把2grams列表变成字符串才能统计！！
print(c)


#方法2：把文本字段变成双词字段为key，频率为value的dict，再用sorted为ngrams.items排序
def ngrams(input, n):
    input = cleanInput(input)
    output = {}
    for i in range(len(input)-n+1):
        ngramTemp = " ".join(input[i:i+n]) #切片并组合为字符串
        if ngramTemp not in output:
            output[ngramTemp] = 0
        output[ngramTemp] += 1
    return output

content = str(urlopen("http://pythonscraping.com/files/inaugurationSpeech.txt").read(),'utf-8') #.read返回bytes
ngrams = ngrams(content, 2)
print(ngrams) #{'legislatures not': 1, 'is applied': 1, 'casual observer': 1, 'in language': 1, 'union--cordial confiding': 1,

sortedNGrams = sorted(ngrams.items(), key = operator.itemgetter(1), reverse=True)
print(sortedNGrams) #[('of the', 213), ('in the', 65), ('to the', 61), ('by the', 41), ('the constitution', 34), ('of our', 29), ('to be', 26)

'''
相关知识点：
sort改变被排序者，sorted不改变
sorted()参数key的lambda用法注意了：
student_tuples = [('john', 'A', 15),('jane', 'B', 12),('dave', 'B', 10),]
sorted(student_tuples, key=lambda student: student[2]) 
更方便的用法：
from operator import itemgetter, attrgetter
sorted(student_tuples, key=itemgetter(2)) 还允许多级排序，key=itemgetter(1,2)

感悟：
为数据按照其使用目的选择合适的组织方式及数据结构，技术是工具，了解不同工具的用法必然好，可以帮助你更精准的选择工具
但是必要时你需要灵活的避开不会处理的，用你掌握的工具去处理问题
就好比这个列表的统计词频并排序的问题，如果在2grams的基础上我并不会统计排序，我可以选择把数据整理成别的结构比如字典，再去用sorted去处理
不要卡在非要用2grams处理这个坎上
后来我通过问大神知道了Counter的用法，再学习提高

这算是我卡着的第一个问题了，以后也一定会出现相似的情况
这大概就是先用不高明的技术写出来，之后慢慢学了新技术后，再去回看之前的代码，能用性能更好/代码更简短/更方便的库和工具处理/更优化的数据结构组织，就算是成长吧
但是千万不能不知变通的卡在一个地方，低级的写法也能解决问题，解决问题优先

思维模式：
观察发现问题----------发现了产生的结果中有很多无意义的常用词/有空格转义字符串字符串/有标点符号
产生明确的处理任务----------剔除/清理
产生任务与多种处理手段选择的处理路径----------【这一步最重要】问题与工具的对应，充分知晓工具的使用场景
通过经验/判断选择一种更好的----------【高手进阶】就像是架构师在技术选型一样，懂得各种工具的特点优缺点，做出做适合问题求解的工具选择
执行----------用文字（类伪代码）描述问题求解思路，问题能分为几个小模块（函数，类），模块接口，不断添加异常处理和特殊条件判断等
例如：

更厉害的大牛他们懂得在各个层面处理问题，因为他们懂得各个层面的工具：
六度分割理论广度优先搜索的性能处理就不是学了Python能搞得了的了，涉及底层的数据结构知识和c++
词频统计问题的规模再大一些到自然语言处理，又要用到spark
甚至他们能从底层硬件架构上面把一个初创公司从无到有架设起来
这就是学习科班基础知识必要的原因吧
再牛的大牛，自己发明工具

路漫漫其修远
'''