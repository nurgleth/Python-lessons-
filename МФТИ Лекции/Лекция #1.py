"""
Простейший алгоритм
"""
a = 2
b = 5
print(a, b)
"""
первый вариант, классический, через одну переменную
"""
tmp = a
a = b
b = tmp
print(a,b)
"""
второй вариант,через две переменные 
"""
a = 2
b = 5
print(a, b)
tmp1 = b
tmp2 = a
a = tmp1
b = tmp2
print(a, b)
"""
третий вариант, множественное присв. через временый кортеж
"""
a = 2
b = 5
print(a, b)
tmp1, tmp2 = b, a
a, b = tmp1, tmp2
print(a, b)
"""либо"""
a = 2
b = 5
print(a, b)
a, b = b, a
print(a, b)

"""
немного теории групп
"""
a = -12//5
print(a)
a = -12%5
print(a)

"""
цикл while
"""
while "условие":  # Заголовок
    "оператор 1"
    "оператор 2" # Тело цикла
    if "что-то":
        break
    "оператор n"
else:
    "после всех итераций"

"""
цикл for
"""

for x in 1, 5 ,2, 4, 3:
    print(x**2)
"генератор range (start, stop, step)"
print (range(1, 10, 1))