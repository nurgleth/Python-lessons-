# Файл makedb.py сохраняет объекты Person в хранилище
from person import Person, Manager # Импортирует наши классы
bob = Person("Bob Smith") # Создание объектов для сохранения
sue = Person("Sue Jones", job="dev", pay=100000)
tom = Manager("Tom Jones", 50000)
import shelve # Использует первые два модуля (dbm,pickle), позволяя сохранять объекты в файлах-хранилищах, обеспечивающих возможность обращения по ключу.
db = shelve.open("persondb") # Имя файла хранилища
for object in (bob, sue, tom): # В качестве ключа использовать атрибут name
    db[object.name] = object # Сохранить объект в хранилище
db.close() # Закрыть после внесения изменений


"""
Работа с хранилищем
"""
import shelve
db = shelve.open("persondb") # Открыть хранилище
print(len(db)) # В хранилище содержится три записи
print(list(db.keys()))  # keys – это оглавление
bob = db["Bob Smith"] # Извлечь объект bob по ключу
print(bob) # Вызовет __str__ из AttrDisplay
print(bob.lastName()) # Вызовет lastName из Person
for key in db: # Итерации, извлечение, вывод
    print(key, "=>", db[key])

for key in sorted(db):
    print(key, "=>", db[key]) # Итерации через отсортированный список ключей
