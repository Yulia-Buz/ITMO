# Задача 1
def task_1():
    a: int = 5
    b: float = 0.07
    c: str = 'Slozhno'
    d: list = ['slozhno']
    e: bool = True

    print(a, "относится к типу ", type(a))
    print(b, "относится к типу ", type(b))
    print(c, "относится к типу ", type(c))
    print(d, "относится к типу ", type(d))
    print(e, "относится к типу ", type(e))
    
task_1()

# Задача 2
def task_2(a: list = [1, 2, 3, 5, 8, 13, 21]) -> list:
    return a[0:3]

print(task_2())

# Это числа Фибоначчи.

# Задача 3
def task_3(a: int) -> int:
    return a * a

print(task_3(5))