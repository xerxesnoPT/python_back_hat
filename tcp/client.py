from socket import *
import time
from threading import Thread
import threading

HOST = '172.16.164.1'
PORT = 12333
BUFSIZ = 1024
ADDR = (HOST, PORT)

#while 1:
#    tcpCliSock = socket(AF_INET, SOCK_STREAM)
#    tcpCliSock.connect(ADDR)
#    data = input('>>')
#    if not data:
#        break
#    tcpCliSock.send('{}\r\n'.format(data).encode('utf-8'))
#    data = tcpCliSock.recv(BUFSIZ)
#    if not data:
#        break
#    print(data.decode('utf-8'))
#    tcpCliSock.close()

def func():
    while True:
        tcpCliSock = socket(AF_INET, SOCK_STREAM)
        tcpCliSock.connect(ADDR)
        data ='dsss {}'.format(threading.currentThread())
        tcpCliSock.send('{}\r\n'.format(data).encode('utf-8'))
        while True:
            data = tcpCliSock.recv(BUFSIZ)
            tcpCliSock.close()
            #print(data.decode('utf-8'))
            break


if __name__ == '__main__':
#    func()
    threads = []
    for i in range(10000):
        t = Thread(target=func)
        threads.append(t)
    for i in range(100):
        threads[i].start()
    for i in range(100):
        threads[i].join()
