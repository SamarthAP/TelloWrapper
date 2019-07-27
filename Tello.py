import threading
import socket
import time

class Tello:

    PORT = 8889
    HOST = ''

    def __init__(self):
        self.address = ('192.168.10.1', 8889)
        self.response = None

        # UDP socket
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.bind((HOST, PORT))

        # Thread for UDP reveicer 
        recvThread = threading.Thread(target=receive)
        recvThread.daemon = True # Thread ends when program ends
        recvThread.start()

    def receive(self):
        while True:
            try:
                self.response, server = sock.recvfrom(1024)
                print((self.response.decode(encoding='utf-8'), server))
            except Exception as e:
                print('Error: ' + e)
                break
