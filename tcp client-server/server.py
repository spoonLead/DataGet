import socket

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

serverName = socket.gethostbyname(socket.gethostname())
serverPort = 12000

serverSocket.bind((serverName, serverPort))
print("The server is ready")

serverSocket.listen(3)

while 1:
    connectionSocket, addr = serverSocket.accept()
    print("Connection received from " + str(addr))
    message = connectionSocket.recv(1024)
    print("Message: " + message.decode("utf-8"))
    connectionSocket.close()
    print("Connection " + str(addr) + " close\n" )
