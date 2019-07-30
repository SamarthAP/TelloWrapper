import threading
import socket
import time
import cv2

class Tello:

    def __init__(self):
        self.PORT = 8889
        self.VIDEO_PORT = 11111
        self.HOST = ''
        self.TIMEOUT = 0.5 # seconds
        self.COMMAND_WAIT = 0.5 # wait 0.5 before next command is sent

        self.address = ('192.168.10.1', 8889)
        self.response = None
        self.last_command_time = time.time()

        # UDP socket
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind((self.HOST, self.PORT))

        # Thread for UDP reveicer 
        self.recv_thread = threading.Thread(target=self.receive)
        self.recv_thread.daemon = True # Thread ends when program ends
        self.recv_thread.start()

    def receive(self):
        while True:
            try:
                self.response, server = self.sock.recvfrom(1024)
                # print((self.response.decode(encoding='utf-8'), server))
            except Exception as e:
                print('Error: ' + e)
                break 
    
    def send_command(self, command):
        # If time since last command is less than 0.5,
        # wait until 0.5 seconds are up
        command_diff = time.time() - self.last_command_time
        if command_diff < self.COMMAND_WAIT:
            time.sleep(command_diff)

        # send command
        new_command_time = time.time()
        self.sock.sendto(command.encode('utf-8'), self.address)

        while self.response is None:
            # If timeout occurs
            if time.time() - new_command_time >= self.TIMEOUT:
                return False 

        new_command_response = self.response.decode(encoding='utf-8')
        print('Response: ' + new_command_response)
        self.response = None
        self.last_command_time = time.time()
        
        return new_command_response
    
    def send_quick_command(self, command):
        self.sock.sendto(command.encode('utf-8'), self.address)
    
    def send_rc_command(self, left_right, forward_backward, up_down, yaw):
        self.send_quick_command('rc %s %s %s %s' % (left_right, forward_backward, up_down, yaw))
    
    def takeoff(self):
        self.send_quick_command('takeoff')
    
    def land(self):
        self.send_quick_command('land')

    def connect_sdk(self):
        self.send_quick_command('command')
