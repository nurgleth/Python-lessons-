"""
Факториал можной пройти цилом for, а можно и рекурсией
"""

def f_r(n_r:int): # рекурсия Факториал
    if n_r == 0:# крайний случай
        return 1
    return f_r(n_r - 1) * n_r
print(f_r(5))

"""
динамеческое программирование не требует функции. создаем массив со значениями
Этот вариант Факториала лучше так как рекурсия хранит ещё и ссылки возварата поэтому по памяти лучше динамическое решение Факториала
"""
n_d = int(input("Ввидите положительное число для вычисления Факториала дин.прог."))
f_d = [1] * (n_d + 1) # начиная с крайнего случая
for i in range(1, n_d + 1):
    f_d[i] = f_d[i - 1] * i
print(f_d)

# Числа Фибоначчи
"""
рекурентно
"""

def fib_r(n:int):
    assert n >= 0 #функция предназначена для положительных чисел и если будет отрицателньое число произодйдёт исключение
    if n <= 1:
        return n
    else:
        return fib_r(n - 1) + fib_r(n - 2)
print(fib_r(10))
"""
Динамически
"""
def fib_d(n:int):
    assert n >= 0 #функция предназначена для положительных чисел и если будет отрицателньое число произодйдёт исключение
    fib = [None] * (n + 1) #создадим массив значений. append делает аллоцирование памяти и не всегда хорошо его использовать
    fib[:2] = [0, 1] # это лучше по памяти чем fib = [0, 1] + [0] * [n - 1] так как мы не создаем много списков
    for k in range(2, n + 1):
        fib[k] = fib[k - 1] + fib[k - 2]
    return fib[n]
print(fib_d(10))