#import socket module
from socket import *
from threading import Thread

def requestHandler(newSocket, clientInfo):
	print("client {} has connected".format(clientInfo))
	try:         
		message =  newSocket.recv(1024)
		#print(message.split())
		filename = message.split()[1]                         
		f = open(filename[1:])
		outputdata = f.read()
		#Send one HTTP header line into socket
		httpHeader = 'HTTP/1.1 200 OK\r\nConnection: close\r\nContent-Type: text/html\r\nContent-Length: %d\r\n\n' % (len(outputdata))
		newSocket.send(httpHeader.encode()) 

		#Send the content of the requested file to the client
		'''
		for i in range(0, len(outputdata)):
			newSocket.send(outputdata[i])
		'''
		newSocket.send(outputdata.encode())
		newSocket.close()
	except IOError:
		#Send response message for file not found
		httpHeader = 'HTTP/1.1 404 Not Found'
		newSocket.send(httpHeader.encode())

		#Close client socket
		newSocket.close() 

def main():
	serverPort = 8888
	serverSocket = socket(AF_INET, SOCK_STREAM) 
	#Prepare a sever socket 
	serverSocket.bind(('', serverPort))
	serverSocket.listen(5)
	while True:     
		#Establish the connection    
		print 'Ready to serve...'     
		connectionSocket, addr =  serverSocket.accept()
		p = Thread(target=requestHandler, args=(connectionSocket, addr))
		p.start()
	serverSocket.close()

if __name__ == '__main__':
	main()