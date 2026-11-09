from socket import AF_INET, SOCK_STREAM, SOL_SOCKET, SO_REUSEADDR, socket
import threading

logPort = 12001
logSocket = socket(AF_INET, SOCK_STREAM)
logSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
logSocket.bind(('localhost', logPort))
logSocket.listen(5)

print('Shared chat log is ready. Start server.py and client.py in other terminals.')

def show_messages(connectionSocket):
    logFile = connectionSocket.makefile('r')
    for message in logFile:
        print(message.rstrip())
    logFile.close()
    connectionSocket.close()

while True:
    connectionSocket, addr = logSocket.accept()
    thread = threading.Thread(target=show_messages, args=(connectionSocket,))
    thread.start()