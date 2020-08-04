from nmap import PortScanner

def portScan(hostName, port):
    nmScan = PortScanner()
    nmScan.scan(hostName, port)
    state = nmScan[hostName]['tcp'][int(port)]['state']
    print('[*] - ' + str(hostName) + 'tcp/'+ str(port)+': ' + state)
