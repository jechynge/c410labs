import socket, threading, random

# Base chatServer class template obtained from Stack Overflow here:
# http://stackoverflow.com/questions/6487772/simple-telnet-chat-server-in-python
#
# Modified by Jordan Ching

HOST = ''
PORT = 51237 

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(4)
clients = [] #list of clients connected
lock = threading.Lock()
random.seed()


class chatServer(threading.Thread):
    def __init__(self, (socket,address)):
        threading.Thread.__init__(self)
        self.socket = socket
        self.address= address

    def run(self):
        lock.acquire()
        clients.append(self)
        lock.release()
        self.socket.send("Welcome to the server. Please enter your username: ")
        while True:
            data = self.socket.recv(1024).rstrip()
            if not data:
                self.username = "AnonymousUser"+str(random.randint(1,1000000000))
                break
            else:
                self.username = data
                break
        print '%s connected with username %s.' % (self.address, self.username)
        self.socket.send("Welcome, %s. Type something and hit 'Enter' to send it to the server.\n" % self.username)
        while True:
            data = self.socket.recv(1024).rstrip()
            if not data:
                break
            self.socket.send(data + " " + self.username + "\n")
            #for c in clients:
            #    c.socket.send(self.username + ": " + data)
        self.socket.close()
        print '%s:%s disconnected.' % self.address
        lock.acquire()
        clients.remove(self)
        lock.release()

while True: # wait for socket to connect
    # send socket to chatserver and start monitoring
    chatServer(s.accept()).start()