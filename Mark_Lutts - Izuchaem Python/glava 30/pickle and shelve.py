"""
Придется держать в уме: классы и их хранение
помимо возможности имитировать взаимодействия в реаль-
ном мире, классы, разработанные для пиццерии, могли бы также ис-
пользоваться как основа базы данных пиццерии.
"""
"""from somefile import someClass
import pickle
object = someClass()
file = open("filename.txt", "wb") # Создать внешний файл
pickle.dump(object, file)   # Сохранить объект в файле

import pickle
file = open("filename.txt", "rb")
object = pickle.load(file) """ # Позднее извлечь обратно

"""
Модуль pickle преобразует объекты, находящиеся в памяти, в последо-
вательности байтов (в действительности – в строки), которые можно
сохранять в файлах, передавать по сети и так далее. При извлечении
объектов происходит обратное преобразование: из последовательности
байтов в идентичные объекты в памяти. Модуль shelve реализует похо-
жую возможность, но он автоматически сохраняет объекты в базе дан-
ных с доступом по ключу, которая предоставляет интерфейс, похожий
на интерфейс словаря:
"""
""" import shelve
object = someClass()
dbase = shelve.open("filename.txt")
dbase["key"] = object       # Сохранить под ключом key

import shelve
dbase = shelve.open("filename.txt")
object = dbase["key"]   """    # Позднее извлечь обратно


from pizzashop_1 import PizzaShop
shop = PizzaShop()
print(shop.server, shop.chef)
import pickle
pickle.dump(shop, open("shopfile.dat", "wb"))

"""
Мы можем сохранить в файле весь составной объект, представляющий
пиццерию, одной инструкцией. Чтобы восстановить его в следующем
сеансе или при очередном запуске программы, также достаточно един-
ственной инструкции. При этом после восстановления таким способом
объекты получают обратно и свои данные, и свою логику работы
"""

import pickle
obj = pickle.load(open("shopfile.dat", "rb"))
print(obj.server, obj.chef)
print(obj.order("Sue"))