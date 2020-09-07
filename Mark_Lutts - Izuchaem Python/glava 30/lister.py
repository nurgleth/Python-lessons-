"""
Создание примесных классов, реализующих вывод
"""
class Spam:
    def __init__(self): # Нет метода __repr__ или __str__
        self.data1 = "food"
X = Spam()
print(X) # По умолчанию: класс, адрес

class ListInstance:
    """
    Примесный класс, реализующий получение форматированной строки при вызове
    функций print() и str() с экземпляром в виде аргумента, через наследование
    метода __str__, реализованного здесь; отображает только атрибуты
    экземпляра; self – экземпляр самого нижнего класса в дереве наследования;
    во избежание конфликтов с именами атрибутов клиентских классов использует
    имена вида __X
    """

    def __str__(self):
        return " < Instance of % s, address % s:\n % s >" % (
            self.__class__.__name__,    # Имя клиентского класса
            id(self),                   # Адрес экземпляра
            self.__attrnames())         # Список пар name=value

    def __attrnames(self):
        result = ""
        for attr in sorted(self.__dict__):  # Словарь атрибутов
            result += "\tname % s = % s\n"% (attr, self.__dict__[attr])
        return result



