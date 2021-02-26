# -*- coding = utf-8 -*-
"""
作者：WandererX

时间：2021年02月25日  16:14:18
"""

import re

pat=re.compile('AA')    #AA为正则表达式，用于验证其他模板

# m=pat.search('CBAA')    #被校验    返回第一次匹配成功的位置 左闭右开


# #没有模式对象
# m=re.search('AA','auisAAbdhh')
# print(m)
# #返回值是None 表示不匹配

#sub
print(re.sub('a','A','ahhajjjdasas'))   #用A替换a
#AhhAjjjdAsAs
#一般在字符串前加r，防止被转义 very安全