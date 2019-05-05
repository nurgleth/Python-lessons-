"""
Основы программирования классов
"""
class FirstClass:
    def setdata(self, value):
        self.data = value
    def display(self):
        print(self.data)

x = FirstClass()
y = FirstClass()

x.setdata("King Arthur")
y.setdata(3.141592653589793)

x.display()
y.display()

x.data = "New value"
x.display()

class SecondClass(FirstClass):
    def display(self):
        print('Current value = "%s"' % self.data)

z = SecondClass()
z.setdata(42)
z.display()

class ThirdClass(SecondClass): # Наследует SecondClass
    def __init__(self, value): # Вызывается из ThirdClass(value)
        self.data = value
    def __add__(self, other): # Для выражения “self + other”
        return ThirdClass(self.data + other)
    def __str__(self): # Вызывается из print(self), str()
        return "[ThirdClass: %s]" % self.data
    def mul(self, other): # Изменяет сам объект: обычный метод
        self.data *= other

a = ThirdClass("abs") # Вызывается новый метод __init__
a.display() # Унаследованный метод
print(a) # __str__: возвращает строку

b = a + "xyz" # Новый __add__: создается новый экземпляр
b.display()
print(b) # __str__: возвращает строку
a.mul(3) # mul: изменяется сам экземпляр
print(a)