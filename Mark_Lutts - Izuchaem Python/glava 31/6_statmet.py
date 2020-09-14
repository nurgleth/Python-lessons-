"""
Статические методы и методы класса
статические методы работают почти так же, как обычные функции, только расположенные внутри
класса, а методы класса получают сам класс вместо экземпляра
"""

class Spam: # Для доступа к данным класса используется статический метод
    """
    Подсчет количества экземпляров с помощью статических методов
    """
    numInstances = 0
    def __init__(self):
        Spam.numInstances += 1
    def printNumInstances():
        print("Number of instances:", Spam.numInstances)
    printNumInstances = staticmethod(printNumInstances)

a = Spam()
b = Spam()
c = Spam()
print(Spam.printNumInstances())
print(a.printNumInstances())

"""
Подсчет экземпляров с помощью методов класса
"""
class Spam_metod:
    """
класс обладает тем же поведением, что и класс
со статическим методом, представленный выше, но в нем используется метод
класса, который в первом аргументе принимает класс экземпляра. Методы
класса автоматически получают объект класса
    """
    numInstances = 0 # Вместо статического метода используется метод класса
    def __init__(self):
        Spam_metod.numInstances += 1
    def printNumInstances(cls):
        print("Number of instances:", cls.numInstances)
    printNumInstances = classmethod(printNumInstances)
"""
Однако, используя методы класса, имейте в виду, что они принимают класс,
самый близкий к объекту вызова. Это влечет за собой ряд важных последствий, 
который оказывают влияние на попытки изменить данные класса через
переданный методу класс
"""

a, b = Spam_metod(), Spam_metod()
print(a.printNumInstances())
print(Spam_metod.printNumInstances())

class Spam1:
    numInstances = 0
    def count(cls): # Счетчик экземпляров для каждого отдельного класса
        cls.numInstances += 1 # cls – ближайший к экземпляру класс
    def __init__(self):
        self.count() # Передаст self.__class__ для подсчета
    count = classmethod(count)
class Sub(Spam1):
    numInstances = 0
    def __init__(self): # Переопределяет __init__
        Spam1.__init__(self)
class Other(Spam1): # Наследует __init__
    numInstances = 0

x = Spam1()
y1, y2 = Sub(), Sub()
z1, z2, z3 = Other(), Other(), Other()
print(x.numInstances, y1.numInstances, z1.numInstances)
print(Spam1.numInstances, Sub.numInstances, Other.numInstances)
