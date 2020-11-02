import socket
import time
import pickle


HEADERSIZE = 10

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1243))
s.listen(5)

while True:
    # now our endpoint knows about the OTHER endpoint.
    clientsocket, address = s.accept()
    print(f"Connection from {address} has been established.")

    d = {1:"hi", 2: "there"}
    msg = pickle.dumps(d)
    msg = bytes(f"{len(msg):<{HEADERSIZE}}", 'utf-8')+msg
    print(msg)
    clientsocket.send(msg)

'''
import socket

#want to use header to send messages
HEADERSIZE = 10
#define socket ovject
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #family type, type of socket
#AF_INET is with IPV4 and SOCK_STREAM is with TCP
s.bind((socket.gethostname(), 1234))
#socket is end point that receives data, socket itself is not the communicat
#endpoint sits at an IP and a port
s.listen(5) #this is a que

while True:
    clientsocket, address = s.accept()
    print(f"Connection from {address} has been established!")

    msg = "Welcome to the server!"
    msg = f'{len(msg)}:<{HEADERSIZE}' + msg
    
    clientsocket.send(bytes(msg,"utf-8")) #send data to client
    # clientsocket.close()
'''
