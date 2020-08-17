from createZip import createZip
from extractZip import extractZip
from optparse import OptionParser
from operator import itemgetter

def main():
    parsedOptions = OptionParser('-f <zipfilename> -d <dictionary>')
    parsedOptions.add_option('-f', '--file', dest='zipFile', help='Add zip file path')
    parsedOptions.add_option('-d', '--dictionary', dest='dictionary', help='Add dictionary file path')
    options, args = parsedOptions.parse_args()
    zipFile = options.zipFile
    dictionary = options.dictionary
    if (zipFile == None or dictionary == None):
        return
    extractZip(zipFile, dictionary)

if __name__ == '__main__': 
    main()