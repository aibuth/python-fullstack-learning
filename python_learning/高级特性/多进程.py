"""
import os
print('Process (%s) starts.. ' % os.getpid())
pid = os.fork()
if pid == 0:
    print('I am child process (%s) and my parent is %s.' % (os.getpid(),os.getppid()))
else:
    print('I (%s) just created a child process (%s).' % (os.getpid(),pid))

由于Windows没有fork调用，上面的代码在Windows上无法运行。而Mac系统是基于BSD（Unix的一种）内核，所以，在Mac下运行是没有问题的，推荐大家用Mac学Python！
有了fork调用，一个进程在接到新任务时就可以复制出一个子进程来处理新任务，常见的Apache服务器就是由父进程监听端口，每当有新的http请求时，就fork出子进程来处理新的http请求。
"""
# from multiprocessing import Process
# import os
# def run_proc(name):
#     print('Child process %s (%s)' % (name, os.getpid()))
# if __name__ == '__main__':
#     print('Parent process %s' % os.getpid())
#     p = Process(target=run_proc, args=('test',))
#     print('Child process will starts')
#     p.start()
#     p.join()
#     print('Child process ends')
#
#
# from multiprocessing import Pool
# import os,time,random
# def long_time_task(name):
#     print('Run task %s (%s)' % (name, os.getpid()))
#     start = time.time()
#     time.sleep(random.random() * 3)
#     end = time.time()
#     print('Task %s run %.2f seconds' % (name, end - start))
#
# if __name__ == '__main__':
#     print('Parent process %s.' % os.getpid())
#     p = Pool(4)
#     for i in range(5):
#         p.apply_async(long_time_task, args=(i,))
#     print('Waiting for all subprocess done...')
#     p.close()
#     p.join()
#     print('All subprocess done.')



"""
很多时候，子进程并不是自身，而是一个外部进程。我们创建了子进程后，还需要控制子进程的输入和输出。
subprocess模块可以让我们非常方便地启动一个子进程，然后控制其输入和输出。
下面的例子演示了如何在Python代码中运行命令nslookup www.python.org，这和命令行直接运行的效果是一样的：
"""
# import subprocess
# print('$ nslookup www.python.org')
# r = subprocess.call(['nslookup','www.python.org'])
# print('Exit code:', r)




# import subprocess
# print('$ nslookup')
# p = subprocess.Popen(
#     ['nslookup'],
#     stdin=subprocess.PIPE,
#     stdout=subprocess.PIPE,
#     stderr=subprocess.PIPE
# )
# output, err = p.communicate(b'set q=mx\nwww.python.org\nexit\n')
# print(output.decode('gbk',errors='replace'))
# print('Exit cede:', p.returncode)


"""
Process之间肯定是需要通信的，操作系统提供了很多机制来实现进程间的通信。Python的multiprocessing模块包装了底层的机制，提供了Queue、Pipes等多种方式来交换数据。
我们以Queue为例，在父进程中创建两个子进程，一个往Queue里写数据，一个从Queue里读数据：
"""

from multiprocessing import Process, Queue
import os, time, random
def write(q):
    print('Process to write: %s' % os.getpid())
    for value in ['A','B','C']:
        print('Put %s to queue...' % value)
        q.put(value)
        time.sleep(random.random())

def read(q):
    print('Process to read: %s' % os.getpid())
    while True:
        value = q.get(True)
        print('Get %s from queue...' % value)

if __name__ == '__main__':
    q = Queue()
    pw  = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    pw.start()
    pr.start()
    pw.join()
    pr.terminate()