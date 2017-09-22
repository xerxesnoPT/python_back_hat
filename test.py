import socket
import threading

def get_tcp():
    target_host = '0.0.0.0'
    target_port = 9999
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((target_host, target_port))
    # client.send("GET / HTTP/1.1\r\nHost: baidu.com\r\n\r\n")
    # print response
    client.send('i am coming')
#
# def get_udp():
#     target_host = '127.0.0.1'
#     target_port = 80
#     client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#     client.sendto('AAABBBCCC', (target_host, target_port))
#     data, addr = client.recvfrom(4096)
#     print data

if __name__ == '__main__':
    Td = []
    for i in range(7):
        send_message = threading.Thread(target=get_tcp)
        Td.append(send_message)
    print Td
    for t in Td:
        t.start()
        print t



