from socket import *
from time import ctime

HOST = ''
PORT = 12333
BUFSIZ = 1024
ADDR = (HOST, PORT)
tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)

while 1:
    print('waitting for connectiong')
    tcpCliSock, addr = tcpSerSock.accept()
    print('{} this is address'.format(addr)) 
    data = ''
    while 1:
        data = tcpCliSock.recv(BUFSIZ)
        if not data or data.decode('utf-8') == 'quit':
            break
        tcpCliSock.send('[{}]-{}'.format(ctime(),data).encode('utf-8'))
    tcpCliSock.close()
    if data.decode('utf-8') == 'quit':
        break

tcpSerSock.close()
