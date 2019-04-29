import socket
import threading

class Node:
    def __init__(self,port=10001):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind(("localhost",port))
        self.socket.listen(5)
        self.cli_socks = {}
        t = threading.Thread(target=self.handle_connect)
        t.start()
    def handle_connect(self):
        while True:
            cli_sock, cli_addr = self.socket.accept()
            print("connected",cli_addr)
            t = threading.Thread(target=self.handle_message,args=[cli_sock])
            t.start()
    def handle_message(self,conn):
        while True:
            recv = conn.recv(4096)
            print(recv)
    def connect(self,addr=("localhost",10001)):
        addr = addr[0].replace("localhost","127.0.0.1"),addr[1]
        cli_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        cli_sock.connect(addr)
        self.cli_socks[addr] = cli_sock
        t = threading.Thread(target=self.handle_message,args=[cli_sock])
        t.start()
    def send_message(self,addr=("localhost",10001),message=""):
        addr = addr[0].replace("localhost","127.0.0.1"),addr[1]
        if not addr in self.cli_socks:
            print("Fuck!!")
            return False
        message = message.encode("utf-8")
        self.cli_socks[addr].send(message)

if __name__ == "__main__":
    n = Node()
    n.connect(("localhost",10001))
    n.send_message(message="test!!")

