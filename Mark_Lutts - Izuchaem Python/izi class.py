class rec: pass # Объект пустого пространства имен
rec.name = "Bob" # Так же для объектов с атрибутами
rec.age = 40
print(rec.name) # Как структура в языке C или запись
x = rec() # Экземпляры наследуют имена из класса
y = rec()
print(x.name, y.name) # Сейчас имена хранятся только в классе

x.name = "Sue" # Но присваивание изменит только объект x
print(rec.name, x.name, y.name)

print(rec.__dict__.keys())

print(list(x.__dict__.keys()))
print(list(y.__dict__.keys()))
"""
Здесь в словаре класса присутствуют атрибуты name и age, которые мы создали
ранее, объект x имеет свой собственный атрибут name, а объект y по-прежнему
пуст.
"""
print(x.__class__)
"""
Каждый экземпляр имеет ссылку на свой наследуемый класс, она назы-
вается __class__, если вам захочется проверить ее:
"""
print(rec.__bases__) # () пустой кортеж
"""
Классы также имеют атрибут __bases__, который представляет собой кортеж
его суперклассов
"""

def upperName(self):
    return self.name.upper() # Аргумент self по-прежнему необходим
"""
Здесь еще ничего не говорится о классе – это простая функция и она может
вызываться как обычная функция при условии, что объект, получаемый ею,
имеет атрибут name (в данном случае имя аргумента self не имеет никакого осо-
бого смысла).
"""
print(upperName(x))

"""
Однако, если эту простую функцию присвоить атрибуту нашего класса, она
станет методом, вызываемым из любого экземпляра (а также через имя самого
класса при условии, что функции вручную будет передан экземпляр):
"""
rec.method = upperName

print(y.method())
print(rec.method(y))

class rec1: pass

pers1 = rec1()
pers1.name = "mel"
pers1.job = "trainer"
pers1.age = 40

pers2 = rec1()
pers2.name = "dave"
pers2.job = "developer"

print(pers1.name, pers2.name)

"""
Наконец, для реализации записи мы могли бы написать более полноценный
класс:
"""
class Person:
    def __init__(self, name, job):
        self.name = name
        self.job = job
    def info(self):
        return (self.name, self.job)

rec1 = Person("mel", "trainer")
rec2 = Person("vls", "developer")

print(rec1.job, rec2.info())