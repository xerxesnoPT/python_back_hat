from collections import deque

def student(name, homeworks):
    for homeworks in homeworks.items():
        yield (name, homeworks[0], homeworks[1])

class Teacher(object):
    def __init__(self, students):
        self.students = deque(students)

    def handle(self):
        while len(self.students):
            student = self.students.pop()
            try:
                homework = next(student)
                print('handling', homework[0], homework[1], homework[2])
            except StopIteration:
                pass
            else:
                self.students.appendleft(student)


def customer():
    print("consumer start")
    r = 'init'
    while True:
        n = yield r
        print(n, r)
        r = 'ok %s' %n

def producer(c):
    print("producer start")
    r = c.send(None)
    n = 0
    while n < 5:
        n += 1
        print('produce %s 个馒头' %n)
        r = c.send(n)
        print(r)
    c.close()

import asyncio

@asyncio.coroutine
def hello():
    print("Hello world!")
    r = yield from asyncio.sleep(10)
    print('hello again!!')

@asyncio.coroutine
def wget(host):
    print('wget %s...' %host)
    connect = asyncio.open_connection(host, 80)
    reader, writer = yield from connect
    header = 'GET / HTTP/1.0\r\nHost: %s\r\n\r\n' %host
    writer.write(header.encode('utf-8'))
    yield from writer.drain()
    while True:
        line = yield from reader.readline()
        if line == b'\r\n':
            break
        print('%s header > %s' %(host, line.decode('utf-8').rstrip()))
    writer.close()


async def do_some_work(x):
    print("Waiting:", x)

def move(n, a, b ,c):
    if n==1:
        print ("%s-----> %s" %(a,c))
    else:
        move((n-1), a,c,b)
        move(1,a,b,c)
        move((n-1),b,a,c)

def triangles():
    l = [1]
    while True:
        l = [1] + [l[j]+l[j+1] for j in range(len(l)-1)] + [1]
        yield l








if __name__ == '__main__':
    n = 0
    for t in triangles():
        print(t)
        n = n+1
        if n==10:
            break





