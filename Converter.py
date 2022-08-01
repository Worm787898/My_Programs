def ten_to_binary(val):
    nums = []
    while True:           #Цикл делит число на два и записывает в список единицы и нули
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
    nums.reverse()        #Переставляет единицы и нули в списке в обратном порядке
    result = str(nums)               
    result = result.replace(", ", "")  #Удаление ненужных символов
    result = result.replace("[", "")
    result = result.replace("]", "")
    return int(result)

print('Конвертер двоичных чисел')
result = ten_to_binary(int(input("Введите целое десятичное число -> ")))
print('Результат:')
print(result)
exit = input()