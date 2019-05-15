"""
Коллектив работников в пицерии (пару классов)
"""
class Employee: # Самый общий класс, реализует поведение общее для всех работников
    def __init__(self, name, salary=0):
        self.name = name
        self.salary = salary
    def giveRaise(self, percent): # метод увеличения зарплаты в процентах
        self.salary = self.salary + (self.salary * percent)
    def work(self):
        print (self.name, "does stuff")
    def __repr__(self): # метод вывода на экран
        return "<Employee: name=%s, salary=%s>" % (self.name, self.salary)

class Chef(Employee): # класс повар наследующий класс Employee (служащий)
    def __init__(self, name):
        Employee.__init__(self, name, salary=50000)
    def work(self):
        print(self.name, "makes food")

class Server(Employee): # Класс официантб наследующий класс Employee(служащий)
    def __init__(self, name):
        Employee.__init__(self, name, salary=40000)
    def work(self):
        print(self.name, "interfacec with customer")

class PizzaRobot(Chef): # класс робот наследующий от повара Chef
    def __init__(self, name):
        Chef.__init__(self, name)
    def work(self):
        print(self.name, "make pizza")

if __name__ == "__main__": # классическая самопроверка класса
    bob = PizzaRobot("bob") # Создать робота с именем bob
    print(bob)              # Вызвать унаследованный метод __repr__
    bob.work()              # Выполнить действие, зависящее от типа
    bob.giveRaise(0.2)      # Увеличить роботу зарплату на 20%
    print(bob)
    print()

    for klass in Employee, Chef, Server, PizzaRobot: # вывод всех экземпляров классов метода work
        obj = klass(klass.__name__)
        obj.work()


