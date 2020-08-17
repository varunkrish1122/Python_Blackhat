from socket import setdefaulttimeout, socket, create_connection, gethostbyname

setdefaulttimeout(20)
socketConnection = socket()
googleIp = gethostbyname('www.google.com')
print(googleIp)
# socketConnection.connect((googleIp,21))
# socketResponse = socketConnection.recv(1024)
# print(socketResponse)
