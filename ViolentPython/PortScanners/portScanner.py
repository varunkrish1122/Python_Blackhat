from socket import *

def scanning(host, port):
    with open('portScanLogger.txt', 'a+') as logger:
            try:
                connectionSocket = socket(AF_INET, SOCK_STREAM)
                connectionSocket.connect((host, port))
                connectionSocket.send(b'ViolentPython\r\n')
                result = connectionSocket.recv(100)
                print(type(result))
                logger.write('Port ' + str(port) + ' is available to open \n')
                print('\t ' + result.decode('utf8') + '\n')
                logger.write('\t ' + result.decode('utf8') + '\n')
                connectionSocket.close()
            except:
                logger.write('Port ' + str(port) + ' is Closed \n')

def portScan(host):
    try:
        tgtIp = gethostbyname(host)
    except:
        print('Enter Host Name '+ host +' not found!! Please Enter new one and try again!!')
        return
    
    try:
        tgtName = gethostbyaddr(tgtIp)
        print('Scans Result for ' + tgtName[0])
    except:
        print('Scans Result for ' + host)
    with open('portScanLogger.txt', 'r+') as logger:
            logger.truncate(0)
    
    for port in [443]:
        print('Started Scanning port [ - ] ' + str(port))
        scanning(host, port)
    