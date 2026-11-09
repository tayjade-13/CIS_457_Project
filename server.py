from email import message
from socket import *
import threading

serverPort = 12000
logPort = 12001
logSocket = socket(AF_INET,SOCK_STREAM)
logSocket.connect(('localhost',logPort))
serverSocket = socket(AF_INET,SOCK_STREAM)

# optional line to quickly reuse the same port number, its not required for the project
serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

serverSocket.bind(('localhost',serverPort))
serverSocket.listen(1)
print('The server is ready to receive.')

connectionSocket, addr = serverSocket.accept()

def recieve_message():
    message = connectionSocket.recv(1024).decode()
    print("\nClient:", message)
    recieve_message()

def send_reply():
    reply = input("Enter message to client: ")

    if reply == "QUIT":
        quit_reply = 'Server has disconnected.'
        logSocket.send(('Server: ' + quit_reply + '\n').encode())
        connectionSocket.send(quit_reply.encode())
        connectionSocket.close()
        serverSocket.close()
        logSocket.close()
        exit()

    logSocket.send(('Server: ' + reply + '\n').encode())
    connectionSocket.send(reply.encode())
    send_reply()

receive = threading.Thread(target=recieve_message)
send = threading.Thread(target=send_reply)

receive.start()
send.start()


