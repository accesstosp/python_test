
#import sys
#if "D:\ZHONGXING\projects\python_test" not in sys.path:
#   sys.path.append("D:\ZHONGXING\projects\python_test")

"""
sys.path 变量的初始值来自如下：
输入脚本的目录（当前目录）。
环境变量 PYTHONPATH 表示的目录列表中搜索。
Python 默认安装路径中搜索。
"""

#import syntax.dataStructs
#除了包含函数定义外，模块也可以包含可执行语句。这些语句一般用来初始化模块。他们仅在 第一次 被导入的地方执行一次。

"""
import syntax.control
control = syntax.control
print(control.m)
control.func()
"""

#from syntax.control import func,m
from org.hzm.syntax.control import *
print(m)
func()


