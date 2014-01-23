import socket, threading, random, re

HOST = ''
PORT = 51238 

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(4)
clients = [] #list of clients connected
lock = threading.Lock()
random.seed()
clientCommand = re.compile('^\/clients$')
messageCommand = re.compile('^\/msg\s(\w+)\s(.+)')


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
        self.socket.send("Welcome, %s. Type something then hit 'Enter' to send it to the server.\nYou can also type '/clients' in order to see a list of connected users.\n" % self.username)
        while True:
            data = self.socket.recv(1024).rstrip()
            if not data:
                break
            elif clientCommand.match(data):
                for c in clients:
                    self.socket.send(c.username+"\n")
            elif messageCommand.match(data):
                command = messageCommand.match(data)
                print("Direct message to"+ command.group(1))
                client = [x.username for x in clients].index(command.group(1))
                print ("Found user "+clients[client].username)
                clients[client].socket.send(">%s: %s"%(self.username, command.group(2)))
            else:
                for c in clients:
                    c.socket.send("%s: %s\n"%(self.username, data))
        self.socket.close()
        print '%s:%s disconnected.' % self.address
        lock.acquire()
        clients.remove(self)
        lock.release()

while True: # wait for socket to connect
    # send socket to chatserver and start monitoring
    chatServer(s.accept()).start()