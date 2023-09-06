# Задача № 2
x = 10
y = 20
if x > y:
    print(x)
else:
    print(y)

# Задача № 3
x = 200
y = 65
if x == y + 135 or x == y - 135:
    print('yes')
else:
    print('no')

# Задача № 4
x = 6
if x in range(3, 6):
    print('весна')
elif x in range(6, 9):
    print('лето')
elif x in range(9, 12):
    print('осень')
else:
    print('зима')

# Задача № 5
a = 16
b = 40
c = 11
if a > 10 and b > 10 and c > 10:
    print('yes')
else:
    print('no')

# Задача № 6
a = -4
b = -2
c = -10
d = -3
e = -20
x = 0
if (a > 0):
    x = x + 1
if (b > 0):
    x = x + 1
if (c > 0):
    x = x + 1
if (d > 0):
    x = x + 1
if (e > 0):
    x = x + 1
print('Количество положительных чисел:', x)

# Задача № 7

def quant_days(a: int, b: int) -> int:
    return (a * 348) + (b * 29)
print(quant_days(2, 3))
