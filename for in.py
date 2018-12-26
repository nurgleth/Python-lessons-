# Оператор for in
# служит для перебора элементов
# функция range() генерирует последовательность начинющаяся с нуля, заканчивая чилом в скобках
# можно вывести пару ключ значений функцией items() после слова "for" нужно указать два парамметра, один для имени ключа, другой, для его значения
# функция zip() нужна для обхода нескольких списков
# функция "enumerate()" выводит все индексы и связанные с ними значения, в качестве парамметра указывается имя списка

# список алфавит
alphabet = ["Z", "E", "O", "G", "L"]
# кортедж животных
zoo = ["zebra", "elephant", "owl", "giraffe", "lion"]
# множество работника
work = {"name": "Alex", "prof": "Python", "position": "jun"}

# "end" позволит сделать горизонтальный список
alphabet.sort()
zoo.sort()
print("\nAlphabet:\t", end="")
for item in alphabet:
    print(item, end="")
print("\nZoo Enumerate:\t", end="")
for item in enumerate(zoo):
    print(item, end="")
print("\nZip zoo and alphabet:\t", end="")
for item in zip (zoo,alphabet):
    print(item,end="")
print("\nwork:")
for key, value in work.items():
    print(key, "=", value)

