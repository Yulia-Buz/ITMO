a: int = 5
b: str = 'строка'
c: list = [1, 2]

def indent(s: str, width: int) -> str:
    return " " * (max(0, width - len(s))) + s

print(indent('123', 123))


def dlina_str(s: str = '') -> int:
    return len(s)

def min_list(a: list, b: list) -> int:
    return max(len(a), len(b))

def my_func(my_list: list):
    my_list.append('test')
    return my_list

print(my_func(['один', 2, 3]))


def my_func2(my_list2: list) -> int:
    result = 0
    for elem in my_list2:
        result = result + elem
    return

print(my_func2([1, 2, 3]))

