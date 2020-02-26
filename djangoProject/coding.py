# -*- encoding: utf-8 -*-
"""
@File    : coding.py
@Time    : 2020/2/5 18:10
@Author  : David
@Contact : admin@mdavid.cn
@Github  : https://github.com/HEUDavid
@Desc    : 编码练习
"""

lst = [lambda x : i * x for i in range(4)]
print([m(2) for m in lst])