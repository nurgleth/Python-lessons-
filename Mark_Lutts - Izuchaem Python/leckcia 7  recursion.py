# Рекурсия

def matryoshka(n):
    if n == 1:
        print("Матрёшечка")
    else:
        print("Верх матрёшки n=", n)
        matryoshka(n-1)
        print("Низ матрёшки n=", n)

print(matryoshka(5))

# Функция для факториала

def d (n:int):
    assert n>=0, "Факториал отрицательный не определён"
    if n == 0:
        return
    return d(n - 1)*n

# Алгоритм Евклида
"""
определение наибльшего общенго делителя для а и b положительных значений
"""
# Первый способ
def gtd (a, b):
        if a == b:
            return
        elif a > b:
            return gtd(a - b, b)
        else: # a < b
            return gtd(b -a, a)

# второй способ
    def gtd (a, b):
        if b == 0:
            return a
        else:
            return gtd (b, a % b)

# третий  способ самый короткий
    def gtd(a, b):
        return a if b == 0 else gtd(b, a % b)

# Быстрое возведение в степень
"""
не отрицательная целая степень n 
"""

# Первый способ
def pow(a:float, n:int):
        return 1 if n == 0 else pow(a, n - 1)*a
 # Второй способ
def pow(a: float, n: int):
     if n == 0:
         return 1
     elif n % 2 == 1: # Для нечётной степени
         return pow(a, n - 1)*a
     else: # Для чётной степени
         return pow(a**2, n // 2)


