import socket
import traceback
from threading import Thread

address = ('127.0.0.1',9999)

class ClientTcp(object):
    def __init__(self):
        self.socket_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket_client.connect(address)
        
    def send_data(self,data):
        # 发送数据:
        self.socket_client.send(data)
        print(self.socket_client.recv(1024).decode('utf-8'))
        self.socket_client.send(b'exit')
        self.socket_client.close() 


def main():
    client = ClientTcp()
    #接收初始消息
    print (client.socket_client.recv(1024).decode('utf-8'))
    data = input()
    data = bytes(data,'utf-8')
    client.send_data(data)

if __name__ == '__main__' :
    for item in range(5):
        t = Thread(target=main)
        print ("the {} threat client start".format(item+1))
        t.start()
        t.join()
        print ("the {} threat client end".format(item+1))