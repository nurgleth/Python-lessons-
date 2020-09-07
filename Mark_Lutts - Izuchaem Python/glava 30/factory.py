"""
Классы – это объекты:
универсальные фабрики объектов
"""
def factory(aClass, *args): # Кортеж с переменным числом аргументов
    """
    ожидает получить объект класса (любого) вместе с одним или более аргу-
    ментами конструктора класса
    :param aClass:
    :param args:
    :return:
    """
    return aClass(*args) # Вызов aClass (или apply, только в 2.6)
class Spam:
    def doit(self, message):
        print(message)
class Person:
    def __init__(self, name, job):
        self.name = name
        self.job = job
    def __repr__(self): # метод вывода на экран
        return "<Employee: name=%s, salary=%s>" % (self.name, self.job)
object1 = factory(Spam) # Создать объект Spam
object2 = factory(Person, "Guido", "guru") # Создать объект Person
print(object1.doit("Hello word"))
print(object2)
