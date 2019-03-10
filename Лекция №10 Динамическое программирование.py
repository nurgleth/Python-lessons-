"""
реализация бинарного поиска в массиве
требования-он должен быть отсртирован
"""
A = [1, 1, 2, 2, 4, 5, 5, 5, 3, 3, 3, 6]
sorted(A)

"""
рекурентная функция искомый элемент назвается key
"""

def left_bound(A, key):
    """
    поиск левой границы
    """
    left = -1
    right = len(A)
    while right - left > 1:
        middle = (left + right) // 2
        if A[middle] < key:
            left = middle
        else:
            right = middle
    return left

def right_bound(A, key):
    """
    поиск правой границы
    """
    left = -1
    right = len(A)
    while right - left > 1:
        middle = (left + right) // 2
        if A[middle] <= key:
            left = middle
        else:
            right = middle
    return right
"""
если левая и правая функция при сравнении отличаются больше чем на 1, то искомое значение присутствует в массиве, если нет, то элемента в массиве не существует
"""

if left_bound(A, 5) != right_bound(A, 5):
    print("Есть элемент массива")
else:
    print("Нету элемента массива")
# используем функцию для ставки в массив
A.append(left_bound(A,5))
print(sorted(A))

# Динамическое программирование
"""def fib(n):
    if n <= 1:
        return (n)
    return fib(n - 1) + fib(n - 2)"""
"""
функция чилса Фибоначи( так писать его нелдьзя)
"""
# как надо реализововать число фибоначи

def fiban(n):
    fib = [0, 1] + [0]*(n - 1)
    for i in range(2, n + 1):
        fib[i] = fib[i - 1] + fib[i - 2]
    return fib[n]
print(fiban(4))

# Задача с кузнечиком
def count_trajectories(N, allowed:list):
    """
числовая шкала от 0 до n и проверка allowed если есть запрещенная точка прыжка если такова имеется
прыки кузнечика с запрезенными точами. Прыгает на +1, +2, +3
    """
    K = [0, 1, int(allowed[2])] + [0] * (N - 3)
    for i in range(3, N + 1):
        K[i] = K[i - 1] + K[i - 2] + K[i - 3]


"""
минимальная стоймость достижения финиша кузнечиком
price[i] цена за посещение клетки
есть крайние и рекурентные случаи
С[i] -cost минимальная стоймость достижения клетки i 
прыгаем всего два раза +1 клетка и +2 клетка
"""
def count_min_cost(N, price:list):
    C = [None, price[1], price[1] + price[2]] + [0]*(N - 2)
    for i in range(3, N + 1):
        C[i] = price[i] + min(C[i - 1], C[i - 2])
    return C[N]

# Двумерные массивы

"""
список списков как НЕ НАДО создавать
"""
A = [[0] * M] * N

"""
ТАК ПРАВИЛЬНО
"""
A = [[0 * M] for i in range(N)]
