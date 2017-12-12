
"""
执行 from org.hzm.syntax import * 时，如果包中的 __init__.py 代码定
义了一个名为 __all__ 的列表，就会按照列表中给出的模块名进行导入。
如果没有定义 __all__ ， from org.hzm.syntax import * 语句不会
从 org.hzm.syntax 包中导入所有的子模块。
"""
__all__ = ["control","module"]