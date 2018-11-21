import socket

serverName = '192.168.0.103'
serverPort = 12000

while 1:
    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientSocket.connect((serverName, serverPort))
    message = input('Your lowercase sentence: ')
    clientSocket.send(message.encode("utf-8"))

    clientSocket.close()
