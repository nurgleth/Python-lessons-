# Написание классов их тестирования, работа с кодом
class Person:
    def __init__(self, name, job=None, pay=0): # Конструктор принимает 3 аргумента
        self.name = name                # Заполняет поля при создании
        self.job = job                  # self – новый экземпляр класса
        self.pay = pay
    def lastName(self):                 # Методы, реализующие поведение экземпляров
        return self.name.split()[-1]    # self – подразумеваемый экземпляр
    def giveRaise(self, percent):
        self.pay = int(self.pay * (1 + percent)) # Изменения придется вносить только в одном месте
    def __str__(self):
        return "[Perscon: %s, %s]" % (self.name, self.pay) # Добавленный метод строка для вывода




class Manager(Person):      # Определить подкласс класса Person
    """def giveRaise(self, percent, bonus=.10):
        self.pay = int(self.pay * (1 + percent + bonus))" Неправильно копирование"""
    def __init__(self, name, pay):
        Person.__init__(self, name, "mgr", pay)
    def giveRaise(self, percent, bonus=.10): # Переопределить для адаптации
        Person.giveRaise(self, percent + bonus) # Правильно: дополняет оригинал

if __name__ == '__main__':              # Только когда файл запускается для тестирования
# реализация самотестирования
    bob = Person('Bob Smith')
    sue = Person('Sue Jones', job='dev', pay=100000)
    print(bob)
    print(sue)
    print(bob.lastName(), sue.lastName())         # Извлечь фамилию
    sue.giveRaise(.10)
    print(sue)                     # Повысить зарплату
    tom = Manager("Tom Jones", 50000) # Экземпляр Manager: __init__
    tom.giveRaise(.10) # Вызов адаптированной версии
    print(tom.lastName()) # Вызов унаследованного метода
    print(tom) # Вызов унаследованного __str__
    print("--All three--")
    for object in (bob, sue, tom): # Обработка объектов обобщенным способом
        object.giveRaise(.10) # Вызовет метод giveRaise этого объекта
        print(object) # Вызовет общий метод __str__