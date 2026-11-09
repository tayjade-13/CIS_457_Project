from ast import While
from socket import *
import threading

serverName = 'localhost'
serverPort = 12000
logPort = 12001
logSocket = socket(AF_INET, SOCK_STREAM)
logSocket.connect((serverName,logPort))
clientSocket = socket(AF_INET, SOCK_STREAM)

clientSocket.connect((serverName,serverPort))

def send_message():
    message = input('Enter message to server: ')

    if message == "QUIT":
        quit_message = 'Client has disconnected.'
        logSocket.send(('Client: ' + quit_message + '\n').encode())
        clientSocket.send(quit_message.encode())
        clientSocket.close()
        logSocket.close()
        exit()

    logSocket.send(('Client: ' + message + '\n').encode())
    clientSocket.send(message.encode())
    send_message()

def receive_reply():
    reply = clientSocket.recv(1024)
    #print ('\nServer:', reply.decode())
    receive_reply()

send = threading.Thread(target=send_message)
receive = threading.Thread(target=receive_reply)

send.start()
receive.start()
