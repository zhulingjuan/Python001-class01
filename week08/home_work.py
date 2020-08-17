from functools import wraps
import time, datetime
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
def fn_timer(function):
    @wraps(function)
    def function_timer(*args,**kwargs):
        t0 = time.time()
        result = function(*args,**kwargs)
        t1 = time.time()
        print ('[finished {func_name} in {time:.2f}s]'.format(func_name = function.__name__,time = t1 - t0))
        return result
    return function_timer
@fn_timer
def download(url):
    # 模拟下载3秒
    print ('start to download from {0}...'.format(url))
    time.sleep(3)
    print ('download finished!')

download('www.baidu.com')    






