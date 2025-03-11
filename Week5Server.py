from socket import *

def sendResponse(connectionSocket: socket, httpVersion: str, statusCode: str, body: str) -> None:
    responseMessage = ""

    responseMessage += f"{httpVersion} {statusCode}\r\n"
    responseMessage += "\r\n"

    connectionSocket.send(responseMessage.encode())

    for char in body:
        connectionSocket.send(char.encode())
    
    connectionSocket.close()
    print("Successfully responded to a request")

serverPort = 6969

serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))

serverSocket.listen(1)

print('Ready to serve...')

while True:
    connectionSocket, addr = serverSocket.accept()
    try:
        requestMessage = connectionSocket.recv(1024).decode().split()

        httpVersion = requestMessage[2]
        filename = requestMessage[1]
        statusCode = "200 OK"
        htmlData = open(filename[1:]).read()

        sendResponse(connectionSocket, httpVersion, statusCode, htmlData)

    except IOError:
        httpVersion = requestMessage[2]
        filename = "notFound.html"
        statusCode = "404 Not Found"

        htmlData = open(filename).read()

        sendResponse(connectionSocket, httpVersion, statusCode, htmlData)
        
serverSocket.close()