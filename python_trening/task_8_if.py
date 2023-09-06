num = 0
if num >= 0:
    print('Число больше или равно 0')
else:
    print('Число отрицательное')

str_1 = 'test'
str_2 = 'test1'

if str_1 in str_2:
    print('Str_2 содержит в себе str_1')
else:
    print('Str_2 не содержит в себе str_1')


num_float = 0
if num_float > 0:
    print('Положительное число')
elif num_float == 0:
    print('Ноль')
else:
    print('Число отрицательное')

num = 5
permit_print = False
if num > 0 and permit_print:
    print('num - положительное число')
elif not permit_print:
    print('Печать запрещена')
#
num = 4
if num >= 1 and num <= 4:
    print('Бакалавр')
elif num < 7:
    print('магистр')
elif num < 10:
    print('Аспирант')
else:
    print('Введите корректный год обучения')


#
x = 56
if x in range(-100, 101):
    print('+')
else:
    print('-')

