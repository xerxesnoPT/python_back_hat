from socketserver import TCPServer, StreamRequestHandler,ThreadingTCPServer
from time import ctime
from threading import Thread
import threading


HOST = ''
PORT = 12333
BUFSIZ = 1024
ADDR = (HOST, PORT)

class MyRequestHandler(StreamRequestHandler):
    def handle(self):
        print('{}...connected from:'.format(self.client_address))
        # print('current{}'.format(threading.currentThread()))
        print(self.rfile.readline().strip().decode('utf-8'))
        resp = input('>>')
        self.wfile.write('[{}]:: {}'.format(ctime(), resp).encode('utf-8'))

#tcpServ = TCPServer(ADDR, MyRequestHandler)
tcpServ = ThreadingTCPServer(ADDR, MyRequestHandler)
print ('waiting for connect..')
# for i in range(2):
    # t = Thread(target=tcpServ.serve_forever)
    # t.daemon = True
    # t.start()
tcpServ.serve_forever()

