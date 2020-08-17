from zipfile import ZipFile
from threading import Thread


extractedPassword = ''
def getCount(number):
    print('Working')
    for number in range(number):
        yield number


def extractFile(zip, password, counterGen):
    decodedPassword = password.decode('utf8').strip('\n')
    counter = next(counterGen)
    global extractedPassword
    try:
        zip.extractall(pwd=password.strip())
        print('[ ' + str(counter) + ' ] ' + '[ - ] ' + 'Success!! - ' + decodedPassword)
        extractedPassword = decodedPassword
    except:                    
        print('[ ' + str(counter) + ' ] ' + '[ - ] ' + 'Failed!! - ' + decodedPassword)

def extractZip(fileName, dictionary):
    print('*************************')
    with ZipFile(fileName, 'r') as zip:
        with open(dictionary, 'rb') as passwordListFile:
            passwordList = passwordListFile.readlines()
            counterGen = getCount(len(passwordList))
            threadList = []
            for password in passwordList:
                t = Thread(target=extractFile, args=[zip, password, counterGen])
                t.start()
                threadList.append(t)
            for thread in threadList:
                thread.join()
            if extractedPassword:
                print('Password Found!! as ' + extractedPassword)
            else:
                print('Try Another Password List!!')