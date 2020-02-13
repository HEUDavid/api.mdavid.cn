# -*- encoding: utf-8 -*-
"""
@File    : checkEnv.py
@Time    : 2020/2/4 22:45
@Author  : David
@Contact : admin@mdavid.cn
@Github  : https://github.com/HEUDavid
@Desc    : 检查项目运行环境
"""

codeStyle = """代码规范
引号的使用
自然语言双引号 机器标志单引号 多行注释用三个双引号
json格式 dict 均使用双引号
正则使用原生双引号 r"..."
单行注释  # 例子
import 文件头部 全局变量之前
换行 函数参数太多 缩进到括号的起始处
命名规范
其他 使用Pycharm自带代码格式化工具
"""


def checkEnv():
    import platform
    print(platform.python_version())


def main():
    print("hello api.mdavid.cn")
    print(codeStyle)
    checkEnv()


if __name__ == '__main__':
    main()
