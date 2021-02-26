# -*- coding = utf-8 -*-
"""
作者：WandererX

时间：2021年02月26日  22:32:07
"""

import xlwt

# workbook=xlwt.Workbook(encoding='utf-8')    #创建workbook对象
# worksheet=workbook.add_sheet('mysheet')      #创建工作表     参数为表单的名字
# worksheet.write(0,0,'hello world')          #参数：行，列，内容
# workbook.save('hello.xls')

#写99乘法表
workbook=xlwt.Workbook(encoding='utf-8')
worksheet=workbook.add_sheet('mysheet')

for i in range(1,10):
    for j in range(1,1+i):
        worksheet.write(i,j,'%d*%d=%d'%(j,i,i*j))

workbook.save('mut.xls')

