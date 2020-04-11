import socket 

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #socket object

# the client doesn't want to bind, but instead connect()
# connect() takes in a tuple of (IP, port). 

s.connect(('0.0.0.0', 1234)) #same port as the server

# To recieve the message from the server:
# recv() takes in 1 param - recv_size - the size/chunk of data you are permitting to recieve at a time
# recv_size of 1024 bytes is big enough for what we are doing. If we were sending massive files, we would need something bigger

message = s.recv(1024) # in bytes

# we recieve bytes and then we decode them
# decode() takes in char encoding format 
print(message.decode('utf-8'))