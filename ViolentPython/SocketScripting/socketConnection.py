from socket import *

def establishConnection(host, port):
    try:
        connectionSocket = socket(AF_INET, SOCK_STREAM)
        connectionSocket.connect((host, port))
        connectionSocket.send(b'SomeString')
        response = connectionSocket.recv(100)
        print(response)
        print(str(port) + '[ - ] Port is open')
    except:
        print(str(port) + '[ - ] Port is closed')

def connect(hostName, ports):
    try:
        hostIp = gethostbyname(hostName)
        print('Host Ip address is: ' + hostIp)
    except:
        print('Provide proper host name!!')
        return

    try:
        hostAddrs = gethostbyaddr(hostIp)
        print('Scaning for ' + hostAddrs[0])
    except:
        print('Scaning for ' + hostIp)

    for port in ports:
        establishConnection(hostName, port)

