# -*- coding = utf-8 -*-
"""
作者：WandererX

时间：2021年02月25日  10:37:04
"""


from bs4 import BeautifulSoup

file=open('./old.html','rb')
html=file.read()
bs=BeautifulSoup(html,'html.parser')

# #利用bs就可以获取HTML文件中的指定内容了！
# print(bs.title)
# #输出：<title>开始学习HTML标签吧</title>
# print(bs.title.string)
# #输出：开始学习HTML标签吧
# # print(bs.a)
# # print(bs.head)
#
# print(type(bs.head))
# #输出结果：<class 'bs4.element.Tag'>
# #1.Tag标签，返回所检索到的第一个内容
#
# print(type(bs.title.string))
# #输出：<class 'bs4.element.NavigableString'>
# #2.NavigableString标签中的内容，字符串
#
# print(type(bs.a.attrs))
# #输出：<class 'dict'> 字典！！键值对一一对应
# print(bs.a.attrs)
# #输出：{'href': 'http://www.w3school.com.cn'} 获取到该标签中的所有属性，返回一个字典
#
#
# print(type(bs))
# #输出：<class 'bs4.BeautifulSoup'>
# #3.BeautifulSoup    表示整个文档    其内容就是HTML文件中的内容
#
# print(type(bs.a.string))
# #额 这里不太对
# #4.Comments注释，输出内容不包含注释，是2的一种特殊情况




#----------------应用-------------------

# #文档的遍历
#
# print(type(bs.head.contents))
# ##<class 'list'>    所有可以直接用下标访问指定内容
#
# #遍历文档树！



#文档的搜索

#1.find_all()   字符串过滤
# t_list=bs.find_all('a')


#search()     正则表达式
# import re
# t_list=bs.find_all(re.compile('a'))

#利用函数进行搜索

# def nameisexit(tag):
#     return tag.has_attr('name')
# t_list=bs.find_all(nameisexit)
#
# for item in t_list:
#     print(item)

#2.kwargs   参数
# t_list=bs.find_all(id='a')


#3.text     文本
# t_list=bs.find_all(text='我是')


#4.limit
# t_list=bs.find_all('p',limit=3)


#5.css选择器
# t_list=bs.select('title')   #通过标签查找
#通过类名查找
#通过ID查找
#通过属性查找
#层级查找
t_list=bs.select('head>title')
print(t_list)



