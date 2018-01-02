## 关于python多线程与多进程

### multiprocessing
*python 是跨平台的，自然页提供了一个跨平台的多进程支持，multiprocessing模块就是跨平台版本的多进程模块*
```python
from multiprocessing import Process
import os
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def netease(name):
  time.sleep(3)
  print 'Run child process %s(%s)...'%(name, os.getpid())

def tencent(name):
  time.sleep(3)
  print 'Run child process %s(%s)...'%(name, os.getpid())

if __name__ == '__main__':
    print 'Parent process id is %s'%os.getpid()
    p = Process(target=netease, args=('chiji',))  #创建子进程时只需传入一个目标函数及其参数
    p1 = Process(target=tencent, args=('wangzhe',))
    print 'Process will start'
    p.start() #用start()方法启动子进程
    p1.start()
    p.join()  #用join()方法等待子进程结束再继续往下运行
    p1.join()
    print 'Process end'  
```

### Pool
*如果要启动大量的子进程，可以使用进程池的方式批量创建子进程*
```python
from multiprocessing import Pool
import os,time,random

def long_time_task(name):
  print 'Run task %s(%s)...'%(name, os.getpid())
  start = time.time()
  time.sleep(random.random() * 3)
  end = time.time()
  print 'Task %s runs %0.2f seconds.' %(name, (end-start))

if __name__ == '__main__':
  print 'Parent process %s.'%os.getpid()
  p = Pool()
  for i in range(10):
    p.apply_async(long_time_task, args=(i,))  #调用方法apply_async()执行进程，传入目标函数和参数
  print 'Waiting for all subprocess done...'
  p.close() #调用close方法之后，就不能网进程池中添加进程了
  p.join()  #调用join方法等待子进程全部执行结束
  print 'All subprocesses done'
  #默认情况下，pool并发执行的进程数等于cpu核数量，当然可以通过p = Pool(n)来设置
```

### 进程间通信
*python的multiprocessing模块包装了底层的机制，提供了Queue、Pipes等多种方式来交换数据。*
```python
from multiprocessing import Queue, Process
import os
import time
import random
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def write(q， lock):
  lock.acquire()  #get lock
  for value in ['a', 'b', 'c', 'd']:
    print 'put value:%s in queue'%value
    q.put(value)
    time.sleep(random.random())
  lock.release() #release lock

def read(q):
  while True：
    value = q.get(True)
    print 'get value:%s from queue'%value

if __name__ == '__main__':
  q = Queue()
  qw = Process(target=write, args=(q,))
  qr = Process(target=read, args=(q,))
  qw.start()
  qr.start()
  qw.join()
  qr.terminate() #qr是一个死循环进程，需要手工terminate
```
**Queue在Pool中不起作用，需要使用Manager类来辅助生成共享队列**
```python
from multiprocessing import Manager
...
if __name__ == '__main__':
  manager = Manager()
  q = manager.Queue()
  lock = manager.Lock() #也可以通过Manager类使用锁机制
  p = Pool()
  p.apply_async(write, args=(q, lock))
  p.apply_async(read, args=(q,))
  p.close()
  p.join()
```

### 关于多线程
*Python的标准库提供了两个模块：thread和threading，thread是低级模块，threading是高级模块，对thread进行了封装。绝大多数情况下，我们只需要使用threading这个高级模块。启动一个线程就是把一个函数传入并创建Thread实例，然后调用start()开始执行*
```python
import sys
import time
import threading
reload(sys)
sys.setdefaultencoding('utf-8')

def loop():
  print 'thread %s is running...'%threading.current_thread().name
  n=0
  while n<5:
    n += 1
    print 'thread %s >>> %s'%(threading.current_thread().name, n)
    time.sleep(1)
  print 'thread %s ended.'%threading.current_thread().name

print 'thread %s is running...'%threading.current_thread().name
t = threading.Thread(target=loop, name='LoopThread')
t.start()
t.join()
print 'thread %s ended.'%threading.current_thread().name
"""
notes:
  1.由于任何进程默认就会启动一个线程，我们把该线程称为主线程(MainThread)，主线程又可以启动新的线程，python的threading模块有一个current_thread()方法，它永远返回当前线程的实例。
  2.多线程必须考虑的一个问题是多个线程改变共享变量，所以python中的多线程使用threading.Lock 来给共享变量使用的时候加锁
  3.Python的线程虽然是真正的线程，但解释器执行代码时，有一个GIL锁：Global Interpreter Lock，任何Python线程执行前，必须先获得GIL锁，然后，每执行100条字节码，解释器就自动释放GIL锁，让别的线程有机会执行。这个GIL全局锁实际上把所有线程的执行代码都给上了锁，所以，多线程在Python中只能交替执行，即使100个线程跑在100核CPU上，也只能用到1个核。
"""
```
