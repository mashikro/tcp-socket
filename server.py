import socket #part of standard library 

# the socket() function returns a socket object whose methods implement the various socket system calls.

# AF_INET is an address family that is used to designate the type of addresses that your socket can 
# communicate with (in this case, Internet Protocol v4 addresses). When you create a socket, you have 
# specify its address family, and then you can only use addresses of that type with the socket.

# SOCK_STREAM means that it is a TCP socket. There are other types

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #socket object

# bind() takes in a tuple of (IP address, port)
# gethostname() grabs the address of my machine aka localhost
# port = 1234 is most likely a port not being used, lower num ports may be busy

# s.bind((socket.gethostname(), 1234)) #listens to just my laptop

s.bind(('0.0.0.0', 1234)) #listens to all incoming connections

# our server needs to -listen- for incoming requests
# listen() takes in a queue - our queue is 5 long
# queue -  could be larger if this server has large incoming num of requests

s.listen(5)

# we will listen forever for a connection
while True:
    #we will accept anybody that connects
    # clientsocket - client's socket object
    # address - where client is coming from/their IP
    clientsocket, address = s.accept()

    print(f'Conneced to IP: {address}')

    # sending info to the clientsocket
    #send() takes in message and you need to specify its type. We are using bytes here
    clientsocket.send(bytes('Hello from the server!', 'utf-8'))
