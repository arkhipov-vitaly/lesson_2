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
i = 0
integer_number = input ('Введите число для расчленения:')
for i in range (0 , len(integer_number)):
    print(integer_number[i])

'''
Задача 6
Найти сумму цифр числа.
'''
i = 0
sum = 0
number = input ('Введите число для суммы цифр:')
for i in range (0 , len(number)):
    sum = sum + int(number[i])
print(sum)


'''
Задача 7
Найти произведение цифр числа.
'''
i = 0
proizvedenie = 1
number = input ('Введите число для произведения цифр:')
for i in range (0 , len(number)):
    proizvedenie = proizvedenie * int(number[i])
print(proizvedenie)

'''
Задача 8
Дать ответ на вопрос: есть ли среди цифр числа 5?
'''
i = 0
number = input ('Введите число и мы определим наличие цифры 5 в нем:')
for i in range (0 , len(number)):
    if int(number[i]) == 5:
        print('Yes')
        break
else: print('No')

'''
Задача 9
Найти максимальную цифру в числе
'''
i = 0
max = 0
number = input ('Введите число и мы найдем в нем максимальную цифру:')
for i in range (0 , len(number)):
    if int(number[i]) > max:
        max = int(number[i])
print(max)

'''
Задача 10
Найти количество цифр 5 в числе
'''
i = 0
m = 0
number = input ('Введите число и мы найдем в нем цифру 5:')
for i in range (0 , len(number)):
    if int(number[i]) == 5:
        m = m + 1
print(m)













