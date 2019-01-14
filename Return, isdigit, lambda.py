# Возвращение значений и Использование обратного вызова
# Возварщения значений выполняются при помощи ключевого слова return и указанием возвращаемого значения
# Isdigit() Строковая функция  возвращает истину, если все символы в строке являются цифрами, и есть по крайней мере один символ, иначе ложь

num = input("Enter the number (1, 2, etc)")

def number (num):
    if not num.isdigit():
        return "Invalid Enter, please try again"
    num = int(num)
    return num * num
print(num, "Squared Is:", number(num))

# Анонимные функции могут содержать лишь одно выражение, но и выполняются они быстрее.
# Анонимные функции создаются с помощью инструкции lambda.
# Ниже представлен пример равносильных значений. Либо запись через def либо аннанимная lambda
"""def square (x):
    return x ** 2
square = lambda x : x ** 2"""

# Пример из трех функций
def function_1 (x):
    return x ** 2
def function_2 (x):
    return x ** 3
def function_3 (x):
    return x ** 4

callback = [function_1 , function_2, function_3]

print( "\nNamed Functions:")
for function in callback:
    print("Result:", function(3))

# Запишем тоже самое при помощи ананимной функции lambda и посмотрим что будет короче

callback_1 = \
[lambda x: x ** 2, lambda x: x ** 3, lambda x: x ** 4]

print("\nAnonymous Functions:")
for function in callback_1:
    print("Result:", function(3))


# Как видно из примера использование анонимной функции lambda иногда упрощает код