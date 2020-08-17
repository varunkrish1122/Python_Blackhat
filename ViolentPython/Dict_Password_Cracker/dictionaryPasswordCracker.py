from passlib import hash

def getEncryptedPassword():
    fileName = 'passwordFile.txt'
    with open(fileName, 'r') as passwordFile:
        passwordLines = passwordFile.readlines()
        victimPasswordLine = passwordLines[0].strip('\n')
        victimName = victimPasswordLine.split(':')[0]
        encryptedPassword = victimPasswordLine.split(':')[1].strip(' ')
        return (victimName, encryptedPassword)
def isPerfectMatch(word, salt, encryptedPassword):
    newEncryptedPassword = hash.des_crypt.encrypt(word,salt=salt)
    return newEncryptedPassword == encryptedPassword

def main():
    victimName, encryptedPassword = getEncryptedPassword()
    with open('Dictionary.txt', 'r') as dictionaryFile:
        dictionaryList = dictionaryFile.readlines()
        salt = encryptedPassword[:2]
        print('**** Stared Password Searching')
        for wordItem in dictionaryList:
            word = wordItem.strip('\n')
            correctPassword = isPerfectMatch(word, salt, encryptedPassword)
            if correctPassword:
                print('Password Found!! for ' + victimName + '!! password is ' + word)
                break
            else:
                print('Password Not Found for ' + victimName + ' ' + 'Searching....')
            
        
if __name__ == '__main__':
    main()
