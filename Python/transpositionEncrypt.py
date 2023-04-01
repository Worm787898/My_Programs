import pyperclip

def main():
    myMessage = input('Enter message to encrypt - ')
    myKey = int(input('Choose key - '))

    ciphertext = encryptMessage(myKey, myMessage)
    
    print('Encrypted message:')
    print(ciphertext + '|')

    pyperclip.copy(ciphertext)

def encryptMessage(key, message):
    ciphertext = [''] * key

    for column in range(key):
        currentIndex = column

        while currentIndex < len(message):
            ciphertext[column] += message[currentIndex]
            currentIndex += key
    
    return ''.join(ciphertext)

if __name__ == '__main__':
    main()
