# -*- coding = utf-8 -*-
"""
作者：WandererX

时间：2021年02月24日  09:41:51
"""

from bs4 import BeautifulSoup   #网页解析 获取数据
import re   #正则表达式 文字匹配
import urllib.request,urllib.error  #制定URL 获取网页数据
import xlwt #Excel操作
import sqlite3  #数据库操作

#定义全局变量 各种规则
findlink=re.compile(r'<a href="(.*?)">')    #这里findlink接受到的是正则里的内容 吗？   !ans:yes
findimage=re.compile(r'<img.*src="(.*?)"',re.S)     #re.s:让换行符包含在所有字符之中
findtitle=re.compile(r'<span class="title">(.*)</span>')
findgrade=re.compile(r'<span class="rating_num" property="v:average">(.*)</span>')
findnum=re.compile(r'<span>(\d*)人评价</span>')        #评分
findcom=re.compile(r'<span class="inq">(.*)</span>')  #概述
findact=re.compile(r'<p class="">(.*?)</p>',re.S)        #主演



def main():
    baseurl='https://movie.douban.com/top250?start='
    #爬取网页
    print(1)
    datalist=geturl(baseurl)
    savepath='.\\moive_top250.xls'  #.\表示直接创建在当前文件夹下
    #保存数据
    savedata(datalist,savepath)
    print('hello')

def geturl(baseurl):
    datalist=[]
    for i in range(0,10):    #刚好是左闭右开 妙啊！ 10页一共
        url=baseurl+'i*25'
        html=askurl(url)    #html用于保存每个界面

        #逐一解析数据
        soup=BeautifulSoup(html,'html.parser')
        for item in soup.find_all('div',class_='item'):     #查找符合要求的字符串 并形成列表
            #print(item)    test：查看item的所有信息
            data=[]
            item=str(item)  #转换成字符串类型
            #获取到影片详情的链接
            link=re.findall(findlink,item)[0]   #soup:find_all;re:findall
            # print(link)   #测试：打印网址成功
            data.append(link)
            img=re.findall(findimage,item)[0]
            data.append(img)
            title=re.findall(findtitle,item)
            if len(title)==2:   #the num of movie is uncertain
                title1=title[0]
                data.append(title1)
                title2=title[1].replace('/',' ')    #剔除无关内容
                data.append(title2)
            else:
                data.append(title[0])
                data.append(' ')    #占位 防止Excel表格移位
            grade=re.findall(findgrade,item)[0]
            data.append(grade)
            num=re.findall(findnum,item)[0]
            data.append(num)
            com=re.findall(findcom,item)
            if len(com)!=0:
                com=com[0].replace('。',' ')
                data.append(com)
            else:
                data.append(' ')
            act=re.findall(findact,item)[0]
            act=re.sub('<br(s+)?/>',' ',act)
            act=re.sub('/',' ',act)
            data.append(act.strip())    #去掉前后的空格

            datalist.append(data)   #上述过程天添加好了一部电影的内容，该步是将这部电影添加到datalist中
            #注意缩进的位置 逻辑关系
    print(datalist)
    return datalist


#获取一个指定URL的网页的HTML
def askurl(url):
    headers={'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4168.3 Mobile Safari/537.36'}
    requst=urllib.request.Request(url=url,headers=headers)
    html='' #先定义一个空的字符串类型的HTML

    try:
        response=urllib.request.urlopen(requst)
        html=response.read().decode('utf-8')    #利用response获取HTML 注意写法！！
        #print(html)

    except urllib.error.URLError as e:  #这里的e应该也是别名
        if hasattr(e,'code'):   #hasattr函数用来检测参数是否含有某种属性
            print(e.code)
        if hasattr(e,'reason'):
            print(e.reason)
    return html




def savedata(datalist,savepath):
    workbook = xlwt.Workbook(encoding='utf-8',style_compression=0)
    worksheet = workbook.add_sheet('mysheet',cell_overwrite_ok=True)
    col=('详情','图片','中文名','外文名','评分','评价人数','概况','相关信息')  #元组诶
    for i in range(0,8):
        worksheet.write(0,i,col[i])     #列名
    for i in range(0,250):
        print('第%d条'%(i+1))
        data=datalist[i]
        for j in range(0,8):
            worksheet.write(i+1,j,data[j])
    workbook.save('movie_top250.xls')


if __name__=="__main__":        #当程序执行时 便于管理代码的主流程 程序执行的入口
    main()
    print('爬取完毕！')