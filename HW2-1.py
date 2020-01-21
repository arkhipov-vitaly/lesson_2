'''
Задача 1
Вывести на экран циклом пять строк из нулей, причем каждая строка должна быть пронумерована.
'''
i = 1
while i < 6:
    print (i,"- 0")
    i = i +1

'''
Задача 2
Пользователь в цикле вводит 10 цифр. Найти количество введеных пользователем цифр 5.
'''
z_num = 0
z = 1
for z in range(10):
    num = input ('Введите цифру от 0 до 9:')
    if num == '5' :
        z_num = z_num + 1
print (z_num)

'''
Задача 3
Найти сумму ряда чисел от 1 до 100. Полученный результат вывести на экран.
'''
i = 0
sum = 0
for i in range(1,101):
    sum = sum + i
print(sum)

'''
Задача 4
Найти произведение ряда чисел от 1 до 10. Полученный результат вывести на экран.
'''
i = 0
proizvedenie = 1
for i in range(1,101):
    proizvedenie = proizvedenie * i
print(proizvedenie)

'''
Задача 5
Вывести цифры числа на каждой строчке.
'''

integer_number = input ('Введите число:')
while integer_number > 0:
    integer_number = integer_number // 10
print(integer_number % 10)









