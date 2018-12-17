# Неизменяемые списки и множества

# Кортедж - это список с неизменяемыми значениями на протяжении всей программы
# Кортедж индексируется с нуля как и список, пример color = ("red", "green")
# К кортеджу можно присвоить элементы и к ним можно обращаться, нужно столько переменнных сколько элементов в кортедже

# Множества - это списки только с уникальными значениями,в других типах, даже в кортедже значения могут повторяться
# Пример множества color = {"red", "green")
# Нельзя обратиться к отдельному элементу множества!
# Для этого существуют специальные методы:
# Метод множества "set.add(x)" - добавляется элемент "х" в множество
# Метод множества "set.update(x,y,z)" - добавляет несколько элементов в множество
# Метод множества "set.copy()" - возвращает копию множества
# Метод множества "set.pop()" - удаляет один элемент из множества случайным образом
# Метод множества "set.discard(i)" - удаляет из множества элемент с порядковым номером "i"
# Метод множества "set1.intersection(set2) - возвращает элементы, принадлежащие обоим множествам
# Метод множества "set1.difference(set2) - возвращает элементы из множества set1, которых нет в set2

# Для определения структуры данных классов списков применяется функция type


zoo = ("zebra", "elephant", "owl", "giraffe", "lion")
print("List:", zoo, "\tAmount:", len(zoo))
print(type(zoo))

color = {"red", "orange", "yellow", "green", "blue", "purple"}
color.add("dark_blue")
print("\nList:", color, "Amount:", len(color))
print(type(color))

# поиск в множестве выполняется функцией in
print("\nred composed in color?", "red" in color)
print("purple composed in color?", "purple" in color)

# удаляем значение
color.discard("orange")
print("\nList:", color, "\tAmount:", len(color))

# удаляем значение рандомное
color.pop()
print("\nList:", color, "\tAmount:", len(color))
a = color.pop()
print(a)

delete_color = {"orange", a}
print("\nList:", delete_color, "\tAmount:", len(delete_color))
print("sum:", delete_color.intersection(color))
print(color)