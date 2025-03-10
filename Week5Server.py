from socket import *

serverPort = 6969

serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))

serverSocket.listen(1)

print('Ready to serve...')

while True:
    connectionSocket, addr = serverSocket.accept()
    try:
        message = connectionSocket.recv(1024).decode()

        filename = message.split()[1]
        file = open(filename[1:])

        outputData = file.read()

        #Send the content of the requested file to the client

        for i in range(0, len(outputData)):
            connectionSocket.send(outputData[i].encode())

        connectionSocket.send("\r\n".encode())
        connectionSocket.close()
    except IOError:
        errorMessage = "404 Not Found"
        connectionSocket.send(errorMessage.encode())
        connectionSocket.close()
        
serverSocket.close()