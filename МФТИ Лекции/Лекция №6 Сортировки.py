"""
A = []
x = int(input())
A.append(x)
n = len(A)
x = A.pop()
"""
"""
append - метод ля объекта А 
len - узнаем длину массива
pop - метод удаляет посоедний элемент
"""

"""
list comprehensions Цикл for списочного ахрактера
"""
"""
A = [x ** 2 for x in range(10)]
"""
#Эквивалентна запись
""" A = []
for x in range(10):
    A.append(x ** 2)

A = [1, 2, 3, 7, 12, 9, 6] #создать список с чётными членами А и возвести их в квадрат
B = []
for x in A:
    if x % 2 == 0:
        B.append(x ** 2)
#Эквивалентна запись
B = [x ** 2 for x in A if x % 2 == 0]
# если надо убрать отрицательные значения, добавляем тернарные операторы
B = [0 if x < 0 else x **2 for x in A if x % 2 == 0] 
"""

"""
Квадратичные сортировки O(N^2) 
"""
# Вставками( insert sort)
# Выбора (choise sort)
# Метод пузырька (bubble sort)

# начнём с функций пустышек
def insert_sort(A):
    """
    Сортировка списка А вставками
    :param A:
    :return:
    """
    N = len(A)
    for top in range(1, N):
        k = top
        while k > 0 and A[k-1] > A[k]:
            A[k], A[k-1] = A[k-1], A[k]
            k -= 1
def choise_sort(A):
    """
    Сортировка списка А выбором
    :param A:
    :return:
    """
    N = len(A)
    for pos in range(0, N-1): # pos - позиция
        for k in range(pos+1, N):
            if A[k] < A[pos]:
                A[k], A[pos] = A[pos], A[k]

def bubbles_sort(A):
    """
    Сортировка списка А методом пузырька
    :param A:
    :return:
    """
    N = len(A)
    for bypass in range(1, N): # bypass количество проходов
        for k in range(0, N-bypass):
            if A[k] > A[k+1]:
                A[k], A[k+1] = A[k+1] + A[k]
# тестирование
def test_sort(sort_algorithm): # sort_algorithm - массив сортировки
    print("Тестируем: ", sort_algorithm.__doc__)
    print("testsace #1: ", end="")
    A = [4, 2, 5, 1, 3]
    A_sorted = [1, 2, 3, 4, 5]
    sort_algorithm(A)
    print("OK" if A == A_sorted else "Fail") # это условный тернарный оператор

    print("testsace #2: ", end="")
    A = list(range(10, 20)) + list(range(0, 10))
    A_sorted = list(range(20))
    sort_algorithm(A)
    print("OK" if A == A_sorted else "Fail")  # это условный тернарный оператор

    print("testsace #3: ", end="")
    A = [4, 2, 4, 2, 1]
    A_sorted = [1, 2, 2, 4, 4]
    sort_algorithm(A)
    print("OK" if A == A_sorted else "Fail")  # это условный тернарный оператор

if __name__ == "__main__":
    test_sort(insert_sort)
    test_sort(choise_sort)
    test_sort(bubbles_sort)


"""
Сортировка подсчётом (connt sort) быстрее и меньше памяти O(N) операций и О(М) памяти где М ко-во элементов
"""
N = [1, 2, 3, 4, 5, 1, 2, 3]
F = [0] * 8 # создаём пустой список длиною в кол-во элементов и считаем сколько цифр в массиве
for i in range(N): # частотный анализ
    x = int(input())
    F[x] += 1
for diget in range(F):
    print(x)
