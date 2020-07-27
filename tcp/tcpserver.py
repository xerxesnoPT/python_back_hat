from socket import *
from time import ctime
import sys, select
import re

HOST = ''
PORT = 12333
BUFSIZ = 1024
ADDR = (HOST, PORT)
from collections import defaultdict
_service_socket = socket()
_service_socket.setsockopt(65535, 4, 1)
_service_socket.bind(ADDR)
_service_socket.listen(5)
_current_in_list = [_service_socket]
_channel = defaultdict(list)
CONFORM_MSG = re.compile(r'^<RID:(\d+)>([\s\S]*?)</RID:\1>')

def broadcast_message(channel_id, sock, message):
    for member in _channel[channel_id]:
        if member is not sock:
            try:
                member.send(message.encode('utf-8'))
            except Exception:
                member.close()
                _current_in_list.remove(member)
                _channel[channel_id].remove(member)

def main():
    while 1:
        readyinput, readyoutput, readyexception = select.select(_current_in_list,[],[])
        for sock in readyinput:
            if sock is _service_socket:
                client, addr = sock.accept()
                _current_in_list.append(client)
                print('Client connected {} === {}'.format(client, addr))
            else:
                try:
                    raw_message = sock.recv(BUFSIZ).decode('utf-8')
                    print(raw_message)
                    if raw_message:
                        rgx_message = CONFORM_MSG.match(raw_message)
                        if rgx_message:
                            channel_id = rgx_message.group(1)
                            message = rgx_message.group(2)
                            if message.strip() == 'quit':
                                raise Exception
                            if sock not in _channel[channel_id]:
                                _channel[channel_id].append(sock)
                                broadcast_message(channel_id, sock, '{} entered room.\r\n'.format(sock.getpeername()))
                            else:
                                broadcast_message(channel_id, sock, '{} say :{}\r\n'.format(sock.getpeername(),message))
                        else:
                            print('invalid formt message', raw_message)
                except Exception as e:
                    broadcast_message(channel_id, sock, '{} leave room.\r\n'.format(sock))
                    print ('Client {} is offline'.format(sock))
                    sock.close()
                    _current_in_list.remove(sock)
                    for channel_id, socks in _channel.items():
                        for _ in socks:
                            if _ is sock:
                                _channel[channel_id].remove(_)
                                break
                        else:
                            continue
                        break
if __name__ == '__main__':
    main()
