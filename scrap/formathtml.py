# 回顾 html 文件格式
# id  class 定位 html
# 最好不要用正则去解析 html 由于 html 的通用格式非常多,可能出现的变化也非常多

from bs4 import BeautifulSoup

exampleFile = open('file/example.html')
exampleSoup = BeautifulSoup(exampleFile, "lxml")
print(type(exampleSoup))

# tag thread
elems = exampleSoup.select('#author')
print(type(elems))

print(len(elems))

print(type(elems[0]))

print(elems[0].getText())  # 内部 html 信息

print(str(elems[0]))  # 字符串标签,包含开始结束标签

print(elems[0].attrs)  # attr 返回字典: 包含字典 id 以及 id 属性值 author

pElems = exampleSoup.select('p')  # 从 html 对象寻找元素列表

#
spanElems = exampleSoup.select('span')

#
print(spanElems[0].get('id'))  # 获取对应属性值
