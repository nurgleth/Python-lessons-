# Стек или очередь LIFO (можно было сохранить и потом использовать как модуль в нахождении корректной скобочной последовательности далее)
""""
Разобраться с doctest в PyCharm
"""
"""
push - положить в стек
pop - достать из стека
size - величига стека
top - верхгяя часть стека
is_empty - возращает правду или ложь,пусть ли стек
"""
"""
делаем юз кейс для стека
clear()
push(1)
push(2)
push(3)
is_empty 
False
pop()
3
pop()
2
pop()
1
is_empty
True
A_stack: на массиве (list)
"""
_stack = []
def puch(x):
    """
    Добавляет элемент х в конец стека
   size = len(_stack)
   push(5)
   len(_stack) - size
   1
   _stack[-1]
   5
    """
    _stack.append(x)

def pop():
    x = _stack.pop() # деллигирование вызова функции pop для метода класса стекпоп, так же можно написать return _stack.pop()
    return x

def clear():
    _stack.clear()

def is_empty():
    return len(_stack) == 0

if __name__== "__main__": # тест с подключение стандартной библиотеки тестирования и она тестирует;сравнивает документ строку с пррграммой
    import doctest
    doctest.testmod(verbose=True)

#Проверка корректности скобочной последовательности
"""
правила корректных скобочнох выражений А = ""; В = (А); С = АВ
Для очередной скобки: если она открывающейся то в стек ее(запоминаем)
а иначе:
    если стек пуст то некоректно
    иначе
    добываю скобку из стека
    и сравниваю,если х не соответствует у то выход
если стек пуст то корректно
иначе нет 
"""
def is_braces_sequence_correct(s: str):
    """
    Проверяет корректность скобочной последовотельности
    из круглых и квадратных скобок () []
    s_braces_sequence_correct ("(([()]))[]")
    True
    s_braces_sequence_correct ("([)]")
     False
    s_braces_sequence_correct ("(")
    False
    s_braces_sequence_correct ("]")
    False
    """
    # в brace типовой поиск нужной подстроки в строке. Асимптотика хуже для больших строк,для них лучше использовать алгоритм Кнута-Морриса-Пратта
    for brace in s: # brace текущая скобка
        if brace not in "()[]": # все остальные символы игнорируем
            continue
        if brace in "([":
            puch(brace)
        else:
            assert brace in ")]", "Ожидалась закрывающая скобка:" + str(brace) # небольшая проверка, что точно будет закрывающиеся скобка
            if len(_stack) == 0:
                return False
            left = _stack.pop()
            assert left in "([",  "Ожидалась открывающая скобка:" + str(brace) # небольшая проверка, что точно будет закрывающиеся скобка
            if left == "(":
                right = ")"
            elif left == "[":
                right = "]"
            if right != brace:
                return False
    return len(_stack) == 0 # такак как это булевский тип, то вернут так или иначе True  или False
    """
     if len(_stack) == 0:
        return True
    else:
        return False
    """
if __name__== "__main__":
    import doctest
    doctest.testmod(verbose=True)