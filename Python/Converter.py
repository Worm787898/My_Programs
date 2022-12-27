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
    

def menu():
    print("Конвертер двоичных чисел by Worm787898 https://github.com/Worm787898")
    print("-----------------------------------------------------------------------")
    time.sleep(0.5)
    while True:
        print("Выберите режим:")
        print("1 - Десятичное в двоичное")
        print("2 - Двоичное в десятичное")
        print("3 - Выход")
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
                break
            else:
                print("Неверный ввод")
        except:
            print("Неверный ввод")
        time.sleep(1.5)
        print("------------------------------------")
        time.sleep(1)    

menu()
