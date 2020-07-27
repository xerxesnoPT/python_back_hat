from socket import *
from time import ctime
import sys, select

HOST = ''
PORT = 12333
BUFSIZ = 1024
ADDR = (HOST, PORT)
tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)
input_list = [tcpSerSock, sys.stdin]

while 1:
    print('waitting for connectiong')
    tcpCliSock, addr = tcpSerSock.accept()
    print('connect from addr {}'.format(addr))
    input_list.append(tcpCliSock)
    while 1:
        readyinput, readyoutput, readyexception = select.select(input_list,[],[])
        for indata in readyinput:
            if indata == tcpCliSock:
                data = tcpCliSock.recv(BUFSIZ)
                if data.decode('utf-8') == 'quit':
                    input_list.remove(tcpCliSock)
                    break
                print(data.decode('utf-8')) 
            else:
                data = input('>>')
                if data == 'quit':
                    tcpCliSock.send(data.encode('utf-8'))
                    input_list.remove(tcpCliSock)
                    break
                tcpCliSock.send(data.encode('utf-8'))
        if not isinstance(data, str):
            data = data.decode('utf-8')
        if data == 'quit':
            break
    tcpCliSock.close()
tcpSerSock.close()
