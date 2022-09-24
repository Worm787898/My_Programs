abcLibre = ['у','9','г',',','е','м','а','р','о','%','ж','н','и','й','ё','6','в','4','_','к','я','э','х','б','?','-',
'.','д','з','ш','0','!','л','ю','ц','щ','п','т','7','2','1','ч','ы','8','ъ','5','ь','ф','с','3',' ']

def shifrovka(message):
    exit1 = ''
    for i in message:
        index = abcLibre.index(i)
        exit1 = exit1 + str(index) + '.'
    return exit1

def deshifrovka(shifr):
    None

print('Добро пожаловать в шифратор Enigma 2.0')
print('Выберите режим:')
print('1 - Шифровка')
print('2 - Дешифровка')
choise = int(input('- '))
if choise == 1:
    print('Введите сообщение:')
    enter_message = input('-')
    print(shifrovka(enter_message))
elif choise == 2:
    print('Введите шифр:')
    enter_shifr = input('-')
    print(shifrovka(enter_shifr))
else:
    print('Неверный ввод')
exit = input('Нажмите Enter для выхода')
