from socket import *

serverName = 'local host'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)

clientSocket.connect((serverName,serverPort))

message = input('Enter message to server: ')
clientSocket.send(message.encode())

reply = clientSocket.recv(1024)
print ('Server:', reply.decode())

clientSocket.close()
