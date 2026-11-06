from email import message
from socket import *
import threading

serverPort = 12000
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
        connectionSocket.send(quit_reply.encode())
        connectionSocket.close()
        serverSocket.close()
        exit()

    connectionSocket.send(reply.encode())
    send_reply()

receive = threading.Thread(target=recieve_message)
send = threading.Thread(target=send_reply)

receive.start()
send.start()


