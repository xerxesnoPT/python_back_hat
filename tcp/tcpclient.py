from socket import *
import select
import sys

HOST = '172.16.164.1'
PORT = 12333
ADDR = (HOST,PORT)
BUFSIZ = 1024
_current_in_list = [sys.stdin]

def prompt():
    sys.stdout.write('<you>')
    sys.stdout.flush()

def gen_message(channel_id, raw_message):
    return '<RID:{}>{}</RID:{}>'.format(channel_id, raw_message, channel_id).encode('utf-8')

def main():
    channel_id = input('<Channel ID>')
    client_socket = socket()
    try:
        client_socket.connect(ADDR)
        _current_in_list.append(client_socket)
        client_socket.send(gen_message(channel_id,''))
    except Exception as e:
        print(e)
        print('Connect failed')
        sys.exit()

    print('Connect to remote host')
    prompt()

    while 1:
        readyInput, readyOutut, readyException = select.select(_current_in_list, [], [])
        for indata in readyInput:
            if indata is client_socket:
                data = indata.recv(BUFSIZ)
                if not data:
                    print('disconnected from chat server')
                    sys.exit()
                else:
                    sys.stdout.write(data.decode('utf-8')+'\r\n')
                    prompt()
            else:
                raw_message = sys.stdin.readline()
                client_socket.send(gen_message(channel_id, raw_message))
                prompt()

if __name__ == '__main__':
    main()
