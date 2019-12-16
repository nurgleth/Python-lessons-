"""
ГЕнерация всех перестановок
"""
def gen_bin (M, prefix=""):
    """
    Генерация перестановок в двоичной СС
    :param M: Длина чисел
    :param prefix:основание с чего начнётся перестановка чисел
    :return:
    """
    if M == 0:
        print(prefix)
        return
    gen_bin(M - 1, prefix + "0")
    gen_bin(M - 1, prefix + "1")

gen_bin(3)

def gen_bin (M, prefix=""):
    """
    Генерация перестановок в двоичной СС теперсь с циклом
    :param M: Длина чисел
    :param prefix:основание с чего начнётся перестановка чисел
    :return:
    """
    if M == 0:
        print(prefix)
        return
    for digit in "0", "1":
        gen_bin(M-1, prefix + digit)
print("")
gen_bin(3)
print("")
def generate_number(N:int, M:int, prefix=None):
    """
    Генерирует все числа (с лидирующими незначащими нулями)
    в N-ричной системе счисления (N <= 10) длины M
    :param N: Система исчислений
    :param M: Длина чисел
    :param prefix: основание счего начнётся перестановка чисел
    :return:
    """
    prefix = prefix or [] # длятого чтобы при погружениии в рекурсию префикс не был равен 0
    if M == 0:
        print(prefix)
        return
    for digit in range (1, N+1):
        prefix.append(digit)
        generate_number(N, M-1, prefix)
        prefix.pop()
generate_number(2, 3)
print("")

def find(number, A):
    """
    Ищет number в А и возвращает True, если такой есть
    False, если такого нет
    :param x:
    :param A:
    :return:
    """
    for x in A:
        if number == x:
            return True
        return False
def generate_permutation(N:int, M:int=-1, prefix=None):
    """
    Генерирует перестоновок N чисел в M позициях, начиная с prefix
    :param N: число чисел
    :param M: сколько ещё позиций осталось
    :return:
    """
    M = N if M == -1 else M   # по умолчанию N чисел в N позициях
    prefix = prefix or []
    if M == 0:
        print(prefix)
        return
    for number in range(1, N+1):
        if find(number, prefix) in prefix:
            continue
        prefix.append(number)
        generate_number(N, M-1, prefix)
        prefix.pop()

generate_permutation(3)
print("")
def generate_permutation1(N:int, M:int=-1, prefix=None):
    """
    Генерирует перестоновок N чисел в M позициях, начиная с prefix
    :param N: число чисел
    :param M: сколько ещё позиций осталось
    :return:
    """
    M = N if M == -1 else M   # по умолчанию N чисел в N позициях
    prefix = prefix or []
    if M == 0:
        print(*prefix, end=", ",sep="") #почему-то перестало работать
        return
    for number in range(1, N+1):
        if find(number, prefix) in prefix:
            continue
        prefix.append(number)
        generate_number(N, M-1, prefix)
        prefix.pop()

generate_permutation1(3)

