import time

def decimal_to_binary(val):
    nums = []
    while True:           
        if val == 1:
            nums.append(1)
            break
        if val % 2 == 0:
            nums.append(0)
            val = val // 2
            continue 
        if val % 2 == 1:
            nums.append(1)
            val = val // 2
            continue

    nums.reverse()        
    result = str(nums)               
    result = result.replace(", ", "")  
    result = result.replace("[", "")
    result = result.replace("]", "")
    return int(result)

def binary_to_decimal(val):
    val = str(val)[::-1]
    x = 0
    result = 0
    for i in val:
        result += int(i) * (2**x)
        x+=1
    return result

def decimal_to_octal(val):
    nums = []
    while True:           
        if val < 8:
            nums.append(val)
            break
        nums.append(val % 8)
        val = val // 8

    nums.reverse()        
    result = str(nums)               
    result = result.replace(", ", "")  
    result = result.replace("[", "")
    result = result.replace("]", "")
    return int(result)

def octal_to_decimal(val):
    val = str(val)[::-1]
    x = 0
    result = 0
    for i in val:
        result += int(i) * (8**x)
        x+=1
    return result

def decimal_to_hexadecimal(val):
    def number_to_letter(number):
        letter = ''
        if number == 10:
            letter = 'A'
        elif number == 11:
            letter = 'B'
        elif number == 12:
            letter = 'C'
        elif number == 13:
            letter = 'D'
        elif number == 14:
            letter = 'E'
        elif number == 15:
            letter = 'F'
        return letter
    
    nums = []
    while True:           
        if val < 16:
            if val >= 10:
                nums.append(number_to_letter(val))
            else:
                nums.append(val)
            break
        if (val % 16) >= 10:
            nums.append(number_to_letter(val % 16))
        else:
            nums.append(val % 16)
        val = val // 16

    nums.reverse()        
    result = str(nums)               
    result = result.replace(", ", "")  
    result = result.replace("[", "")
    result = result.replace("]", "")
    result = result.replace("'", "")
    return result

def hexadecimal_to_decimal(val):
    def letter_to_number(letter):
        number = 0
        if letter == 'A':
            number = 10
        elif letter == 'B':
            number = 11
        elif letter == 'C':
            number = 12
        elif letter == 'D':
            number = 13
        elif letter == 'E':
            number = 14
        elif letter == 'F':
            number = 15
        return number
    
    val = str(val)[::-1]
    x = 0
    result = 0
    for i in val:
        if any(c.isalpha() for c in i):
            result += letter_to_number(i) * (16**x)
        else:
            result += int(i) * (16**x)
        x+=1
    return result
    

def main():
    print("Конвертер двоичных чисел by Worm787898 https://github.com/Worm787898")
    print("-----------------------------------------------------------------------")
    time.sleep(0.5)
    while True:
        print("Выберите режим:")
        print("1 - Десятичное в двоичное  10->2")
        print("2 - Двоичное в десятичное  2->10")
        print("3 - Десятичное в восьмеричное  10->8")
        print("4 - Восьмеричное в десятичное  8->10")
        print("5 - Десятичное в шестнадцатеричное  10->16")
        print("6 - Шестнадцатеричное в десятичную  16->10")
        print("7 - Выход")
        time.sleep(0.5)
        choose = input(" -> ")
        try:
            if choose == "1":
                number = int(input("Введите целое десятичное число -> "))
                print("Результат: " + str(decimal_to_binary(number)))
            elif choose == "2":
                number = int(input("Введите целое двоичное число -> "))
                print("Результат: " + str(binary_to_decimal(number)))
            elif choose == "3":
                number = int(input("Введите целое десятичное число -> "))
                print("Результат: " + str(decimal_to_octal(number)))
            elif choose == "4":
                number = int(input("Введите целое восьмеричное число -> "))
                print("Результат: " + str(octal_to_decimal(number)))
            elif choose == "5":
                number = int(input("Введите целое десятичное число -> "))
                print("Результат: " + str(decimal_to_hexadecimal(number)))
            elif choose == "6":
                number = input("Введите целое шестнадцатеричное число -> ")
                print("Результат: " + str(hexadecimal_to_decimal(number)))
            elif choose == "7":
                break
            else:
                print("Выход")
        except:
            print("ERROR")
        time.sleep(1.5)
        waiting = input('Нажмите ENTER для продолжения')
        print("------------------------------------")
        time.sleep(1)    

if __name__ == '__main__':
    main()
