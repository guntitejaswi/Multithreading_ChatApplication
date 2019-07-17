# Python TCP Client B
import socket

host = socket.gethostname()
port = 2004
BUFFER_SIZE = 2000
c2msg = input("tcpClientB: Enter message/ Enter exit:")

tcpClientB = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpClientB.connect((host, port))

while c2msg != 'exit':
    tcpClientB.send(c2msg.encode())
    data = tcpClientB.recv(BUFFER_SIZE)
    if not data:
        print("Server closed the connection")
    print("Server > ", data.decode())
    c2msg = input("Me > ")

tcpClientB.close()
