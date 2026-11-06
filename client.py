from socket import *

serverName = 'localhost'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)

clientSocket.connect((serverName,serverPort))

def Talk():
    message = input('Enter message to server: ')

    if message == "QUIT":
        quit_message = 'Client has disconnected.'
        clientSocket.send(quit_message.encode())
        clientSocket.close()
        exit()

    clientSocket.send(message.encode())

    reply = clientSocket.recv(1024)
    print ('Server:', reply.decode())
    Talk()

Talk()
