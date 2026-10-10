from socket import *

serverPort = 12000
serverSocket = socket(AF_INET,SOCK_STREAM)

# optional line to quickly reuse the same port number, its not required for the project
serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

serverSocket.bind(('localhost',serverPort))
serverSocket.listen(1)
print('The server is ready to receive.')

connectionSocket, addr = serverSocket.accept()
     
message = connectionSocket.recv(1024).decode()
print("Client:", message)

reply = input("Enter message to client: ")
connectionSocket.send(reply.encode())
    
connectionSocket.close()
serverSocket.close()
