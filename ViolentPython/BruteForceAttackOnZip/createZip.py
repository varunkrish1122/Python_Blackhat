from zipfile import ZipFile
import os

def getFilePaths(directory):
    return [os.path.join(root, fileName) for root, directories, files in os.walk(directory) for fileName in files]

def createZip(directory, zipName=''):
    zipFileName = zipName
    if not zipName: zipFileName = directory
    filePaths = getFilePaths(directory)
    with ZipFile(zipFileName + '.zip', 'w') as zip:
        print('Creating Zip!!')
        for file in filePaths:
            print('Compressing ' + file)
            zip.write(file)
            zip.setpassword(pwd=bytes('1234', 'utf-8'))
        print('Created Zip!!')
        zip.setpassword(pwd=bytes('1234', 'utf-8'))
        print('Setting Password as', bytes('1234', 'utf-8'))