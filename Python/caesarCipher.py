import pyperclip

message = input('Enter message : ')

key = int(input('Enter crypt-key : '))

mode = input('Choose: \n encrypt or decrypt : ') # задать 'encrypt' или 'decrypt'

SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.`~@#$%^&*()_+-=[]}{|;:<>,/'

translated = ''

for symbol in message:
    if symbol in SYMBOLS:
        symbolIndex = SYMBOLS.find(symbol)
        if mode == 'encrypt':
            translatedIndex = symbolIndex + key
        elif mode == 'decrypt':
            translatedIndex = symbolIndex - key
        if translatedIndex >= len(SYMBOLS):
            translatedIndex = translatedIndex - len(SYMBOLS)
        elif translatedIndex < 0:
            translatedIndex = translatedIndex + len(SYMBOLS)
        
        translated = translated + SYMBOLS[translatedIndex]
    else:
        translated = translated + symbol

print('Message translated and copyed to clipboard:')
print(translated)
pyperclip.copy(translated)