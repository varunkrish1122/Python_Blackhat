from optparse import OptionParser
from socketConnection import connect

def main():
    parser = OptionParser()
    parser.add_option('-H', '--host', dest='hostName', help='Please provide host name', type='string')
    parser.add_option('-p', '--ports', dest='ports', help='Please provide ports', type='string')
    options, args = parser.parse_args()
    hostName = options.hostName
    ports = [int(port.strip(' ')) for port in options.ports.split(',')]
    if hostName == None or ports == None: return
    connect(hostName, ports)


if __name__ == '__main__':
    main()