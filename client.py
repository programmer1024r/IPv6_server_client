# Client
# Get address info
# socket.getaddrinfo("www.python.org", 80, 0, 0, socket.SOL_TCP)

# create a IPv6 socket
# ourSocket = socket.socket(socket.AF_INET6, socket.SOCK_STREAM, 0)
# Connect to a server that is on that port
# ourSocket.connect(('2001:888:2000:d::a2', 80, 0, 0))
import socket

# create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

# get local machine name
host = socket.gethostname()                           
print(f"host name: {host}")

port = 9999

# connection to hostname on the port.
s.connect((host, port))                               

# Receive no more than 1024 bytes
tm = s.recv(1024)                                     

s.close()

print(f"The time got from the server is {tm.decode()}")
