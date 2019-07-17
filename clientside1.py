# Python TCP Client A
import socket

host = socket.gethostname()
port = 2004
BUFFER_SIZE = 2000
c1msg = input("tcpClientA: Enter message/ Enter exit:")

tcpClientA = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpClientA.connect((host, port))

while c1msg != 'exit':
    tcpClientA.send(c1msg.encode())
    data = tcpClientA.recv(BUFFER_SIZE)
    if not data:
        print("Server closed the connection")
    print("Server > ", data.decode())
    c1msg = input("Me > ")

tcpClientA.close()
