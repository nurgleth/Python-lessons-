# Цикл "for"  выполняется гораздо быстрее цикла "while".
# Этот цикл проходится по любому итерируемому объекту (например строке или списку), и во время каждого прохода выполняет тело цикла.

for a in range(1, 5):
    for b in range(1, 5):
        print("Running i =", a, "b=", b)


# Оператор "continue"
# Оператор "continue" начинает следующий проход цикла, минуя оставшееся тело цикла (for или while)
print()
for a in range(1, 5):
    if a == 3:
        continue
    for b in range(1, 5):
        print("Running i =", a, "b=", b)

# Оператор "break" досрочно прерывает цикл.

print()
for a in range(1, 5):
    if a == 3:
        break
    for b in range(1, 5):
        print("Running i =", a, "b=", b)

# Слово "else", примененное в цикле for или while, проверяет, был ли произведен выход из цикла инструкцией break, или же "естественным" образом.
# Блок инструкций внутри "else" выполнится только в том случае, если выход из цикла произошел без помощи "break".

print()
for a in range(1, 5):
    if a == 5:
        break
else:
    print("Цифры 5 в строке нет")
    for b in range(1, 5):
        if b == 6:
            break
    else:
        print("Цифры 6 в строке нет")
