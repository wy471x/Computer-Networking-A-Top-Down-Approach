#import socket module
from socket import *

serverPort = 8888
serverSocket = socket(AF_INET, SOCK_STREAM) 
#Prepare a sever socket 
serverSocket.bind(('', serverPort))
serverSocket.listen(1);
while True:     
	#Establish the connection    
	print 'Ready to serve...'     
	connectionSocket, addr =  serverSocket.accept()
	try:         
		message =  connectionSocket.recv(1024)
		filename = message.split()[1]                          
		f = open(filename[1:])
		outputdata = f.read()
		#Send one HTTP header line into socket
		httpHeader = 'HTTP/1.1 200 OK\r\nConnection: close\r\nContent-Type: text/html\r\nContent-Length: %d\r\n\n' % (len(outputdata))
		connectionSocket.send(httpHeader.encode()) 

		#Send the content of the requested file to the client
		for i in range(0, len(outputdata)):
			connectionSocket.send(outputdata[i])
		connectionSocket.close()
	except IOError:
		#Send response message for file not found
		httpHeader = 'HTTP/1.1 404 Not Found'
		connectionSocket.send(httpHeader.encode())

		#Close client socket
		connectionSocket.close()             
serverSocket.close()