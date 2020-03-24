"""
создадим массив из 1000 элементов, ввидём пять из них от 1-5, ноль будет нашим стопом
"""
A = [0] * 1000
top = 0 # наш стоп элемент,как получим 0 на вводе с клавиатуры,закончится цикл
x = int(input())
while x != 0:
    A[top] = x
    top += 1
    x = int(input())
for k in range(4, -1, -1): # цикл фор пробежит диапазон от 4 до 0 включая это будет номер элемента массива А и выведет их наэкран
    print(A [k])

"""

"""
N = int(input())
C = [0] * N
B = [0] * N
for k in range(N):
    C[k] = int(input())
for k in range(N):
    B[k] = C[k] # из массива C кладём занчения в массив В
D = list(C) # создаю явным образом список С и капирую туда значения А"""

def array_search(A:list, N:int, x:int):
    """
    Осуществляет поиск числа х в массиве А в диапазоне от 0 до N-1 включительно
    Возвращает индекс элемента х в массиве А
    или - 1, если такого нет.
    Если в массиве несколько одинаковых элементов, равных х
    то вернуть индекс первого по счёту
    :param A: Массив
    :param N: Диапазон
    :param x: Элемент массива
    :return:
    """
    for k in range(N):
        if A[k] == x:
            return k
    return -1
# тест функции
def test_array_search():
    A1 = [1, 2, 3, 4, 5] # первый тест
    m = array_search(A1, 5, 8)
    if m == -1:
        print("test1 - ok")
    else:
        print("test1 - fail")

    A2 = [-1, -2, -3, -4, -5] # второй тест
    m = array_search(A2, 5, -3)
    if m == 2:
        print("test2 - ok")
    else:
        print("test2 - fail")
    A3 = [10, 20, 30, 30, 10] # третий тест
    m = array_search(A3, 5, 10)
    if m == 0:
        print("test3 - ok")
    else:
        print("test3 - fail")
test_array_search()

"""
функция инвертирующая массив
"""
def invert_array(A:list, N:int):
    """
    Обращение массива (поворот задом-наперёд
    в рамках индексов от 0 до N-1
    :param A:
    :param N:
    :return:
    """
    for k in range(N//2): # делим на 2 для обмена двух переменных
        A[k] = A[N -1 -k] =  A[N -1 -k] = A[k]

def test_invert_array(): # текст функция
    A3 = [1, 2, 3, 4, 5]  # первый тест
    print(A3)
    invert_array(A3, 5)
    print(A3)
    if A3 == [5, 4, 3, 2, 1]:
        print("test3 - ok")
    else:
        print("test3 - fail")

    A4 = [0, 0, 0, 0, 0, 0, 0, 10]  # второй тест
    print(A4)
    invert_array(A4, 8)
    print(A4)
    if A4 == [10, 0, 0, 0, 0, 0, 0, 0]:
        print("test4 - ok")
    else:
        print("test4 - fail")

test_invert_array()

"""
циклический сдвиг 
"""
# сдвиг влево
def invert_array_left(A:list, N:int):
    A5 = [0, 1, 2, 3, 4]
    tmp = A5[0] # выкладываем нулевой объект в отдельный ящик
    for k in range(N-1):
        A5[k] = A5[k + 1]
    A[N-1] = tmp # возвращаем обратно нулевой объект
# сдвиг вправо
def invert_array_raght(A:list, N:int):
    A6 = [0, 1, 2, 3, 4]
    tmp = A6[N-1] # выкладываем последний объект в отдельный ящик
    for k in range(N-2, -1, -1):
         A6[k + 1] = A6[k]
    A[0] = tmp # возвращаем обратно нулевой объект
#Решето Эратосфена
"""
A = [True]*N
A[0] = A[1] = False
for k in range(2, N):
    if A[k]:
        for m in range(2*k, N, k):
            A[m] = False
for k in range(N):
    print(k,"-", "простое" if A[k] else "состовное")"""