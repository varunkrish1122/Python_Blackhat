from optparse import OptionParser
from nmapConnection import portScan
def main():
    parser = OptionParser()
    parser.add_option('-H', '--host', dest='hostName', type='string', help='Provide host site')
    parser.add_option('-p', '--ports', type='string', dest='ports', help='Provide ports comma seperate')
    options, args = parser.parse_args()
    hostName = options.hostName
    ports = options.ports
    if hostName == None or ports == None: return
    scanPorts = ports.split(',')
    for port in scanPorts:
        portScan(hostName, port)


if __name__ == '__main__':
    main()
