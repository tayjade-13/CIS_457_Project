from ast import While
from socket import *
import threading

serverName = 'localhost'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)

clientSocket.connect((serverName,serverPort))

def send_message():
    message = input('Enter message to server: ')

    if message == "QUIT":
        quit_message = 'Client has disconnected.'
        clientSocket.send(quit_message.encode())
        clientSocket.close()
        exit()

    clientSocket.send(message.encode())
    send_message()

def receive_reply():
    reply = clientSocket.recv(1024)
    print ('\nServer:', reply.decode())
    receive_reply()

send = threading.Thread(target=send_message)
receive = threading.Thread(target=receive_reply)

send.start()
receive.start()
