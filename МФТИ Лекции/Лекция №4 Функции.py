def hello():
    print("Hello, world")
hello()

def hello1(name): # name - формальный параметр
    print("Hello,", name)
hello1("John") # "John" - фактический параметр

def hello2(name = "World"): # name - формальный параметр с пассивом
    print("Hello,", name)
hello2("John1") # "John" - фактический параметр

"""
функция принимающая на вход два параметра и возвращающие наибольшее значение
"""
def max2(x, y):
    if x > y:
        return x
    return y
print(max2(10, 5))

"""
функция принимающая на вход три параметра и возвращающие наибольшее значение
"""
def max3(x, y, z):
    return max2(x, max2(y, z))
print(max3(10, 5, 11))

"""
именнованый парметр
"""
def hello_separated(name = "World", separator = "-"):
    print("Hello", name, sep=separator)
hello_separated(separator="***", name="John") # порядок не важен

"""
метод грубой силы, парочка алгоритмов
"""
def is_simple_number(x):
    """ определяет, является ли число простым. X- целое положительное число.
    Если простое, то возвращает True, a инча - False"""
    divisor = 2
    while divisor < x:
        if x % divisor == 0:
            return False
        divisor += 1
    return True
print(is_simple_number(4))

"""
алгоритм факторизации или разложения на множетели
"""
def factorize_number(x):
    """Раскладывает число на множетели.
    Печатает их на экран. х - целое положительное число. """
    divisor = 2
    while x > 1:
        if x % divisor == 0:
            print(divisor)
            x //= divisor #делим на делитель
        else:
            divisor += 1
print(factorize_number(1024))

