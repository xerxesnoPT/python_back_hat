from socket import *
import select
import sys

HOST = '172.16.164.1'
PORT = 12333
BUFSIZ = 1024
ADDR = (HOST, PORT)
tcpCliSock = socket(AF_INET, SOCK_STREAM)
tcpCliSock.connect(ADDR)
input_list = [tcpCliSock, sys.stdin]


#while 1:
#    data = input('>>>')
#    tcpCliSock.send(data.encode('utf-8'))
#    data = tcpCliSock.recv(BUFSIZ)
#    print(data.decode('utf-8'))

while 1:
    readyInput, readyOutut, readyException = select.select(input_list, [], [])
    data = ''
    for indata in readyInput:
        if indata == tcpCliSock:
            data = tcpCliSock.recv(BUFSIZ)
            print(data.decode('utf-8'))
            if data.decode('utf-8') == 'quit':
                break
        else:
            data = input('plz input >>')
            if data == 'quit':
                tcpCliSock.send(data.encode('utf-8'))
                break
            tcpCliSock.send(data.encode('utf-8'))
    if data=='quit':
        break
tcpCliSock.close()
