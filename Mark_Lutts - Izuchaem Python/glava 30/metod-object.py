"""
Методы – это объекты:
связанные и несвязанные методы
"""
class Spam:
    def doit(self, message):
        print(message)

"""
В обычной ситуации мы создаем экземпляр и сразу же вызываем его метод для
вывода содержимого аргумента
"""
object1 = Spam()
object1.doit("hello world 1")

"""
Однако в действительности попутно создается объект связанного метода – как
раз перед круглыми скобками в вызове метода. Т.е. мы можем получить свя-
занный метод и без его вызова. Квалифицированное имя object.name – это вы-
ражение, которое возвращает объект. В следующем примере это выражение
возвращает объект связанного метода, в котором упакованы вместе экземпляр
(object1) и метод (Spam.doit). Мы можем присвоить этот связанный метод дру-
гому имени и затем использовать это имя для вызова, как простую функцию:
"""
object1 = Spam()
x = object1.doit            # Объект связанного метода: экземпляр+функция
x("Hello world 2")          # То же, что и object1.doit(‘...’)

"""
С другой стороны, если для получения метода doit использовать имя класса,
мы получим объект несвязанного метода, который просто ссылается на объект
функции. Чтобы вызвать метод этого типа, необходимо явно передавать экзем-
пляр класса в первом аргументе
"""
object1 = Spam()
t = Spam.doit               # Объект несвязанного метода
t(object1, "Hello world 3") # Передать экземпляр

"""
Те же самые правила действуют внутри методов класса, когда используются
атрибуты аргумента self, которые ссылаются на функции в классе. Выражение
self.method возвращает объект связанного метода, потому что self – это объект
экземпляра
"""

class Eggs:
    def m1(self, n):
        print(n)
    def m2(self):
        x = self.m1         # Еще один объект связанного метода
        x(42)               # Выглядит как обычная функция
Eggs().m2()

"""
В Python 3.0 несвязанные методы являются функциями
При вызове метода через имя класса передавать ему экземпляр
требуется, только если он ожидает получить его
"""
class Selfless:
    def __init__(self, data):
        self.data = data
    def selfless(arg1, arg2): # Простая функция в 3.0
        return arg1 + arg2
    def normal(self, arg1, arg2): # Ожидает получить экземпляр при вызове
        return self.data + arg1 + arg2
X = Selfless(2)
print("class Selfless")
print(X.normal(3, 4)) # Экземпляр передается автоматически
print(Selfless.normal(X, 3, 4)) # Метод ожидает получить self передается вручную
print(Selfless.selfless(3, 4)) # Вызов без экземпляра: работает в 3.0, но завершается ошибкой в 2.6!

class Number:
    def __init__(self, base):
        self.base = base
    def double(self):
        return self.base * 2
    def triple(self):
        return self.base * 3
x = Number(2) # Объекты экземпляров класса
y = Number(3) # Атрибуты + методы
z = Number(4)
print("class Number")
print(x.double())  # Обычный непосредственный вызов
acts = [x.double, y.double, y.triple, z.double] # Список связанных методов
for act in acts: # Вызовы откладываются
    print(act()) # Вызов как функции

"""
простые функции, определенные с помощью инструкции def или lambda, экзем-
пляры, наследующие метод __call__, и связанные методы экземпляров могут
обрабатываться и вызываться одинаковыми способами
"""
def square(arg):
    return arg ** 2 # Простые функции (def или lambda)
class Sum:
    def __init__(self, val): # Вызываемые экземпляры
        self.val = val
    def __call__(self, arg):
        return self.val + arg
class Product:
    def __init__(self, val): # Связанные методы
        self.val = val
    def method(self, arg):
        return self.val * arg

sobject = Sum(2)
pobject = Product(3)
actions = [square, sobject, pobject.method] # Функция, экземпляр, метод
print("square")
for act in actions: # Все 3 вызываются одинаково
    print(act(5)) # Вызов любого вызываемого объекта с 1 аргументом
print(actions[-1](5)) # Индексы, генераторы, отображения
print([act(5) for act in actions])
print(list(map(lambda act: act(5), actions)))


