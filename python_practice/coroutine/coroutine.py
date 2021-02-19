# -*- coding: utf-8 -*-
import time
import asyncio
import threading
"""
协程
相比于多线程，协程的特点在于它使用一个线程来完成并发任务，多任务切换由程序自己控制。在IO密集型任务中，可以把耗时长的IO操作做成异步处理。
根本区别：多进程与多线程性能更多取决于机器的性能，但协程则更多依赖程序员自身的能力。
协程的优势：
1. 协程中程序的切换不是依靠线程切换，而是通过程序自己控制。因此没有线程切换的开销，效率更高。
2. 协程不涉及锁机制。因为协程是单线程，不存在同时写变量的冲突，在协程中控制共享资源不加锁，只需要判断状态就好了。所以效率进一步提高。
如果想要利用多核CPU，那么可以采用多进程+协程的方式，充分提升性能。
"""


# --------------------------------------------------------------------------
# 使用yield和send()实现协程
# --------------------------------------------------------------------------
def consumer():
    print("start task")
    while True:
        a = yield "now change to producer"
        time.sleep(2)
        print("consumer is working....{} times".format(a))


def producer(t):
    next(t)  # 启动producer
    n = 0
    while n < 3:
        print("-------------------")
        print("producer is working....{} times".format(n))  # producer 执行
        time.sleep(2)
        print("now change to consumer")
        ret = t.send(n)  # consumer 执行
        print(ret)
        n += 1


c = consumer()  # c成为了一个生成器
producer(c)  # 执行producer

# 上面的代码首先通过next函数将c这个生成器激活，执行到yield并暂停。
# 然后执行producer
# send()函数可以重新激活yield下面的语句，并同时将里面的参数赋值给yield左边的变量。


# --------------------------------------------------------------------------
# 使用asyncio库实现Python协程
# asyncio 是python3.4引入的标准库，直接内置了对异步IO的支持。其本质是一个消息循环
# 从asyncio获取一个EventLoop引用，然后把需要执行的协程扔给它里面去执行即可。
# event_loop: 程序会开启一个无限的循环，程序员将一些函数注册到事件循环上
# coroutine：一个协程对象，也就是被装饰器（或者async关键字）定义的函数。调用时并不会立即执行，而是返回一个协程对象。
# task：任务是对协程进行进一步封装。
# future：代表将来执行或者没有执行的任务的结果（同task类似）
# --------------------------------------------------------------------------
@asyncio.coroutine
def walk(n, steps):
    start = 0
    while start < steps:
        print("学生{}往前走".format(n), threading.current_thread())  # 通过输出可以看到两个coroutine都是由同一个线程运行的
        ret = yield from asyncio.sleep(2)  # 这里模拟一个耗时的io操作
        print("学生{}摔了一跤".format(n), threading.current_thread())
        start += 1


loop = asyncio.get_event_loop()  # 获取loop
tasks = [walk(1, 3), walk(2, 3)]  # 两个协程
loop.run_until_complete(asyncio.gather(*tasks))   # asyncio.gather可以将所有协程封装成task，run_until_complete将阻塞直到所有任务都完成
loop.close()

# 上面的代码，当第一个任务执行完"学生往前走"之后，会卡在yield from那里。yield from 会交出当前函数的控制权，此时并不会等待sleep的时间，而是会将当前任务挂起，执行下一个任务。直到
# sleep时间到了或者其他的任务都挂起了，返回值给yield from，然后继续执行第一个任务的后续代码。
print("----------------------------------------------------------------------------------------------------------------")


# --------------------------------------------------------------------------
# 通过task.result()的方式可以直接获取已经完成了的task的返回值（通过return返回）
# run_until_complete内置了回调函数
# --------------------------------------------------------------------------
async def run():  # 把@asyncio.coroutine改成async，语法更简明。同理yield from也可以替换成await关键字
    await asyncio.sleep(1)
    return "run!!"

loop2 = asyncio.new_event_loop()  # 获取一个新的loop，刚才的loop已经被上一个用例close了
c2 = run()
task2 = loop2.create_task(c2)  # 将协程封装成一个task
print(task2)  # pending
loop2.run_until_complete(task2)
print(task2)  # finished
print(task2.result())
loop2.close()


# 也可以手动绑定回调函数，获取自己想要的结果（不推荐）
async def climb():
    await asyncio.sleep(1)
    return "climb!!"


def callback(future):
    print("call back!")
    print(future.result())
    return future.result()


loop3 = asyncio.new_event_loop()
c3 = climb()
task3 = loop3.create_task(c3)
task3.add_done_callback(callback)
loop3.run_until_complete(task3)
loop3.close()
















