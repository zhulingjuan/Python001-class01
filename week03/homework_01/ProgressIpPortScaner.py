# 如何查看端口是否开放 https://blog.csdn.net/IChocolateKapa/article/details/23941967
# 如何使用ping命令https://stackoverflow.com/questions/2953462/pinging-servers-in-python
# 进程池中的队列https://my.oschina.net/yangyanxing/blog/296052
# lock vs RLock https://blog.csdn.net/davidsu33/article/details/51385965
# pmap.py -n 4 -f ping -ip 192.168.0.1-192.168.0.100

from multiprocessing import Process,Queue,Pool
import multiprocessing
import os, time, random,socket,getopt,sys

def getoptValue(optname):
    opts,args = getopt.getopt(sys.argv[1:],'-n:-f:-ip:',['processN=','ping=','ips='])
    for opt_name,opt_value in opts:
        if optname == opt_name:
            if opt_name in ('-n','--processN'):
                #print("[*] processN is ",opt_value)
                return opt_value
            if opt_name in ('-f','--ping'):
                #print("[*] ping is ",opt_value)
                return opt_value
            if opt_name in ('-ip','--ips'):
                #print("[*] ip is ",opt_value)
                return opt_value

def IsOpen(ip,port):
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    try:
        s.connect((ip,int(port)))
        s.shutdown(2)
        #利用shutdown()函数使socket双向数据传输变为单向数据传输。shutdown()需要一个单独的参数，
        #该参数表示了如何关闭socket。具体为：0表示禁止将来读；1表示禁止将来写；2表示禁止将来读和写。
        print(port)
        print('is open')
        return True
    except:
        print(port)
        print('is down')

def IsOpenPorts(ip):
    for i in range(1024) :
        IsOpen(ip,i)



# 写数据进程执行的代码:
def write(q,lock,ips):
    # ip 要转换，我慢慢转
    x = ips.split('-'); 
    for tags in x:
        print(tags)   
    lock.acquire() #加上锁
    # 替换成输入的
    for value in ['61.135.169.125','10.253.212.42']:
        q.put(value)        
    lock.release() #释放锁  

# 读数据进程执行的代码:
def read(q):
    while True:
        if not q.empty():
            value = q.get(False)
            print(value)
            try:
                response = os.system("ping -c 1 " + value)
            except Exception as e:
                print(e)
                break 
            if response == 0:
                print ('ip is open')
                #扫描端口
                IsOpenPorts(value)
            else:
                print ('ip is down')
            time.sleep(random.random())
        else:
            break

if __name__=='__main__':
    hostname  = getoptValue('-n')
    ips = getoptValue('--ips')
    manager = multiprocessing.Manager()
    q = manager.Queue()
    lock = manager.RLock() #为什么不是RLock就会报错（pylint报错）
    p = Pool(int(hostname))
    pw = p.apply_async(write,args=(q,lock,ips)) 
    time.sleep(random.random())     
    pr = p.apply_async(read,args=(q,))
    p.close()
    p.join()
    
