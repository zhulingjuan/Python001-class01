# 作业一：
# 区分以下类型哪些是容器序列哪些是扁平序列，哪些是可变序列哪些是不可变序列：
# 容器序列 collections.deque dict list tuple
# 扁平序列 str
# 可变序列 collections.deque dict list tuple
# 不可变序列 str

# 作业二：
# 自定义一个 python 函数，实现 map() 函数的功能。

def mymap3(func,list1):
    L = []
    for n in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
        L.append(func(n))
    return L    

# 作业三：
# 实现一个 @timer 装饰器，记录函数的运行时间，注意需要考虑函数可能会接收不定长参数。







