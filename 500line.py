import socket
from selectors import DefaultSelector, EVENT_WRITE
def fetch(url):
    sock = socket.socket()
    sock.connect(('baidu.com', 80))
    request = 'GET {} HTTP/1.0\r\nHost: baidu.com\r\n\r\n'.format(url)
    sock.send(request.encode('ascii'))
    response = b''
    chunk = sock.recv(4096)
    while chunk:
        response += chunk
        chunk = sock.recv(4096)

    # Page is now downloaded.
    print(response)

selector = DefaultSelector()

sock = socket.socket()
sock.setblocking(False)
try:
    sock.connect(('baidu.com', 80))
except BlockingIOError:
    pass

def connected():
    selector.unregister(sock.fileno())
    print('connected!')

selector.register(sock.fileno(), EVENT_WRITE, connected)

def loop():
    while 1:
        events = selector.select()
        for event_key, event_mask in events:
            callback = event_key.data
            callback()
loop()


