from employees_1 import PizzaRobot, Server

class Customer:                         # Класс клиента заказа
    def __init__(self, name):
        self.name = name
    def order (self, server):
        print(self.name, "orders from",  server)
    def pay (self, server):
        print(self.name, "pays from item to",  server)

class Oven:                             # Класс печь
    def bake(self):
        print("oven bakes")

class PizzaShop:                        # это контейнер и контроллер – это конструктор, который создает и встраивает экземпляры классов работников, написанные нами в предыдущем разделе, а также экземпляры класса Oven, который определен здесь.
    def __init__(self):
        self.server = Server("Pat")     # Встроить другие объекты
        self.chef = PizzaRobot("Bob")   # Робот по имени Bob
        self.oven = Oven()

    def order(self, name):
        customer = Customer(name)       # Активизировать другие объекты
        customer.order(self.server)     # Клиент делает заказ официанту
        self.chef.work()
        self.oven.bake()
        customer.pay(self.server)

if __name__ == "__main__":
    scene = PizzaShop()                 # Создать составной объект
    scene.order("Homer")
    print("главное блюдо")              # Имитировать заказ клиента Homer
    scene.order("Shaggy")               # Имитировать заказ клиента Shaggy

"""
просто замените имена существи-
тельные классами, глаголы – методами, и вы получите первый черновой на-
бросок проекта
"""