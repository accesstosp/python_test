
def f(a, L=[]):
    """要警告: 默认值只被赋值一次。"""
    L.append(a)
    return L
print(f(1))
print(f(2))
print(f(3))


def concat(*args, sep="/"):
    """函数调用(定义)中参数位置：位置参数->可变参数列表->关键字参数(默认参数值)"""
    return sep.join(args)
print(concat("earth", "mars", "venus"))
print(concat("earth", "mars", "venus", sep="."))


# 参数列表的分拆
args = [3, 6]
print(list(range(*args)))

def parrot(voltage, state='a stiff', action='voom'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.", end=' ')
    print("E's", state, "!")
d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}
parrot(**d)


def make_incrementor(n):
    """Lambda"""
    return lambda x: x + n
f = make_incrementor(42)
print(f(0))
print(f(1))