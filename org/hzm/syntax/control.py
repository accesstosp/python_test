
def func():
    # 循环的 else 子句在未出现 break 时运行
    for n in range(2, 10):
        for x in range(2, n):
            if n % x == 0:
                print(n, 'equals', x, '*', n//x)
                break
        else:
            print(n, 'is a prime number')

m = {x: x**2 for x in (2, 4, 6)}


"""
此代码只有在模块作为 “main” 文件执行时才被调用
如果模块被导入，不会执行这段代码
"""
if __name__ == "__main__":
    import sys
    print(sys.argv)
