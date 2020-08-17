from optparse import OptionParser
from portScanner import portScan

def main():
    parser = OptionParser()
    parser.add_option('-s', '--hostSite', dest='tgtHost', type='string', help='Enter host name')
    options, args = parser.parse_args()
    host = options.tgtHost
    if host == None: return
    portScan(host)
    
if __name__ == '__main__':
    main()