"""
Рекурсия
"""

# Матрёшка

def matryoshka(n):
    if n == 1:
        print("Матрёшечка")
    else:
        print("Верх матрёшки n=", n)
        matryoshka(n-1)
        print("Низ матрёшки n=", n)

matryoshka(5)

"""
Рисуем рекурсию квадрата внитри квадрата
"""

"""alpha = 0.2 # Глобальная константа для уменьшения координат отезка нового квадрата
def fractal_rectangle(A, B, C, D, deep=10): # deep это глубина рекурсии по умолчанию А и т.д. координаты точек квадрата
    if deep < 1:
        return
    """

#создаём временные переменнные М и N и цикл пробегающий по кортеджам А,B и тд создавая пары точек используюя graphics для python
"""
    for M, N in (A,B), (B,C), (C,D), (D,A)
     gr.Line(gr.Point(*M), grPoint(*N)). draw(window)# *А развертовывание итерируемого объекта
    A1 = (A[0]*(1 - alpha) + B[0]*alpha, (A[1]*(1 - alpha) + B[1]*alpha)
    B1 = (B[0]*(1 - alpha) + C[0]*alpha, (B[1]*(1 - alpha) + C[1]*alpha)
    C1 = (C[0] * (1 - alpha) + D[0] * alpha, (C[1] * (1 - alpha) + D[1] * alpha)
    D1 = (D[0] * (1 - alpha) + A[0] * alpha, (D[1] * (1 - alpha) + A[1] * alpha)
    fractal_rectangle(A1, B1, C1, D1, deep-1)
fractal_rectangle((100, 100), (500, 100), (500, 500), (100, 500) """

"""
Факториал 
"""
def f(n:int):
    assert n >= 0, "Факториал отрицательных не определён " # assert оператор проверки вызывающий ошибку
    if n == 0:
        return 1
    return f(n - 1)*n

"""
Алгоритм Евклида (наибольший общий делитель)
"""
def gcd(a, b):
    if a == b:
        return a
    elif a > b:
        return gcd(a - b, b)
    else: # a < b
        return gcd(a, b - a)

def gcd1(a, b):
    """
    Тот эе алгоритм Евклида но с наибольшим общим делителем
    :param a:
    :param b:
    :return:
    """
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def gsd2(a, b):
    """
    ещё более короткая запись алгоритма
    :param a:
    :param b:
    :return:
    """
    return a if b == 0 else gsd2(b, a % b)

"""
быстрое возведение в стемень рекурсией
"""
def pow (a:float, n:int):
    if n == 0:
        return 1
    else:
        return pow(a, n - 1)*a

def pow1 (a:float, n:int):
    """
    модифицируем для чётных степеней или понижаем на 1 если неёчтное
    :param a:
    :param n:
    :return:
    """
    if n == 0:
        return 1
    elif n % 2 == 1: # для нечётных
        return pow(a, n - 1)*a
    else: # n - чётное
        return pow(a ** 2, n // 2)

print(11%3)