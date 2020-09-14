"""
Свойства класса
свойства – это тип объектов, который присваивается именам
атрибутов класса. Они создаются вызовом встроенной функции property, которой передаются три метода
(обработчики операций чтения, присваиванияи удаления), и строкой документирования –
если в каком-либо аргументе передается значение None, следовательно, эта операция не поддерживается.
"""
class classic:
    def __getattr__(self, name):
        if name == "age":
            return 40
        else:
            raise AttributeError

x = classic()
print(x.age) # Вызовет метод __getattr__
#print(x.name) # Вызовет метод __getattr__
class newprops(object):
    def getage(self):
        return 50
    def setage(self, value):
        print("set age:", value)
        self._age = value
    age = property(getage, setage, None, None)
x = newprops()
print(x.age) # Вызовет метод getage
x.age = 42
print(x) # Вызовет метод setage
print(x._age) # Нормальная операция извлечения; нет вызова getage
x.job = "trainer" # Нормальная операция присваивания; нет вызова setage
print(x.job) # Нормальная операция извлечения; нет вызова getage