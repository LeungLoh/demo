import socket
from threading import Thread
import time
import traceback
import sys

address = ('127.0.0.1',9999)
max_connent = 5


class ServerTcp(object):
    def __init__(self):
        # 建立连接
        self.socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.socket_server.bind(address)
        self.socket_server.listen(max_connent)


    def bulid_connent(self):
        while True:
            client,addr = self.socket_server.accept()
            print('Accept new connection from {}...'.format(addr))
            t = Thread(target=self.tcplink,args=(client,addr))
            t.start()


    def tcplink(self,sock,addr):
        sock.send(b'Welcome!')
        while True:
            data = sock.recv(1024)
            time.sleep(1)
            if not data or data.decode('utf-8') == 'exit':
                break
            print ("Accept data {} from {}".format(addr,data))
            sock.send(('Hello, %s!' % data.decode('utf-8')).encode('utf-8'))
        sock.close()
        print('Connection from %s:%s closed.' % addr)

def main():
    server = ServerTcp()
    print("running.....")
    server.bulid_connent()


if __name__ == '__main__':
    main()