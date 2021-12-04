# Server
import socket                                         
import time

# create a socket object
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

# get local machine name
host = socket.gethostname()                           
print(f"host name: {host}")

port = 9999                                           

# bind to the port
serversocket.bind((host, port))                                  

# queue up to 5 requests
serversocket.listen(5)                                           

while True:
    # establish a connection
    clientsocket, addr = serversocket.accept()      

    print(f"Got a connection from {addr}")

    # Get current time
    currentTime = time.ctime(time.time()) + "\r\n"

    clientsocket.send(currentTime.encode())
    clientsocket.close()
