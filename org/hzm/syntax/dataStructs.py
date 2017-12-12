
#使用原始字符串
raw = r'C:\some\name'
# 切片
print(raw[:2] + raw[2:])
# word[2:] = 'py' 字符串不可以被更改，而列表可以
# 从右边数起
print(raw[-1])


# 列表
l = [1,2]
l.append(3) # l[len(l):] = [3]
t = [4,5]
l.extend(t) # l[len(l):] = t
print(l[0])
print(l.index(1)) #返回列表中第一个值为 3 的元素的索引
l.copy() # l[:]
print(l[1:3]) #[1,3)
del l[1:3]
del l
print([(x, y) for x in [1,2,3] for y in [3,1,4] if x != y])
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]
print([[row[i] for row in matrix] for i in range(4)])
for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)


# 元组，不可变的
empty_tuple = ()
singleton = 'hello',


# 集合
empty_set = set()
s = {x for x in 'abracadabra' if x not in 'abc'}


# 字典
tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 4127
tel['jack']

dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
dict(sape=4139, guido=4127, jack=4098)

m = {x: x**2 for x in (2, 4, 6)}
for k, v in m.items():
    print(k, v)

questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print('What is your {0}?  It is {1}.'.format(q, a))