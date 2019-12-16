

N = int(input("enter nuber:"))
flag = False
for i in range(N):
    flag = (N % 10 == 0) or flag
print(flag)

"""
Проверяем все личисла делятся на 10
"""
flag = True
M = int(input("enter nuber:"))

for i in range(M):
    flag = flag and M % 10 == 0
print(flag)

"""
вложенные и посдледовательные if-ы
"""
x = int(input())
if x == 1:
    print("да")
if x == 2:
    print("да")
# эквивалентная запись
if x == 1 or x == 2:
    print("да")

#далее
if x % 2 == 0:
    if x % 3 == 0:
        print("на 6")
#эквивалентна
if x % 2 == 0 and x % 3 == 0:
    print("на 6")

"""
каскадные условные конструкции
"""

"""
числа на прямой, А меньше нуля, В до пяти, С до 10, Д больше 10
"""
x = int(input())

if x < 0:
    print("A")
elif x < 5: # x>5
    print("B")
elif x < 10:
    print("C")
else: print("D")