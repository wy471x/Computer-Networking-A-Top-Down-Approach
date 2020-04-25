import http.client
import sys
from socket import *

'''
	HTTP Client has two implemented methods.
	1. Using http.client module
	2. Using socket 
'''

#'''
#First implementation by using http.client module
conn = http.client.HTTPConnection(sys.argv[1], sys.argv[2]);
conn.request('GET', '/' + sys.argv[3])
print(conn.getresponse().read().decode())
conn.close()
#'''

#'''
#Second implementation by using socket
MAXBYTES = 65536
def main():
	serverName = sys.argv[1]
	serverPort = int(sys.argv[2])
	clientSocket = socket(AF_INET, SOCK_STREAM)
	clientSocket.connect((serverName, serverPort))
	httpHeader = ('GET\r\n/' + sys.argv[3] + '\r\nHTTP/1.1\r\n'
				+ 'Host: ' + sys.argv[1] + ':' + sys.argv[2] + '\r\n'
				+ 'Accept: text/html,application/xhtml+xml,application/xml'
				+ ';q=0.9,image/webp,*/*;q=0.8\r\n'
				+ 'Accept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2\r\n'
				+ 'Accept-Encoding: gzip, deflate\r\n'
				+ 'Connection: keep-alive\r\n')
	clientSocket.send(httpHeader.encode())
	responseData = clientSocket.recv(MAXBYTES)
	#print(responseData)
	if responseData.decode().split()[1] == '200':
		responseData = clientSocket.recv(MAXBYTES).decode()
		print(responseData)
	else:
		print(responseData.decode().split()[-3] + ' ' 
				+ responseData.decode().split()[-2] + ' '
				+ responseData.decode().split()[-1] + '.')
	clientSocket.close()

if __name__ == '__main__':
	main()
#'''