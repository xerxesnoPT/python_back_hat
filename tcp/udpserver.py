from socket import *
from time import ctime

HOST = ''
PORT = 12333
BUFSIZ = 1024
ADDR = (HOST, PORT)
udpSerSock = socket(AF_INET, SOCK_DGRAM)
udpSerSock.bind(ADDR)

while 1:
    print('waitting for message')
    message, addr = udpSerSock.recvfrom(BUFSIZ)
    print('{} this is address'.format(addr)) 
    udpSerSock.sendto('[{}]-{}'.format(ctime(), message).encode('utf-8'), addr)
    if message.decode('utf-8') == 'quit':
        break
udpSerSock.close()
