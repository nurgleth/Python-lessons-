'''
Перегрузка операторов
'''
class Number:
    def __init__(self, start): # Вызов Number(start)
        self.data = start
    def __sub__(self, other): # Выражение: экземпляр - other
        return Number(self.data - other) # Результат – новый экземпляр

if __name__ == '__main__':
    X = Number(5) # Number.__init__(X, 5)
    Y = X - 2 # Number.__sub__(X, 2)
    print(Y.data) # Y - новый экземпляр класса Number
'''
Доступ к элементам по индексу и извлечение
срезов: __getitem__ и __setitem__
'''
class Indexer:
     def __getitem__(self, index):
        return index ** 2

'''
 __getitem__ вызывается не только при выпол-
нении операции обращения к элементу по индексу, но и при извлечении сре-
зов.
'''

class Indexer1:
    data = [5, 6, 7, 8, 9]
    def __getitem__(self, index): # Вызывается при индексировании или извлечении среза
        print('getitem:', index)
        return self.data[index] # Выполняет индексирование или извлекает среза
if __name__ == '__main__':
    X = Indexer()
    print(X[2])  # Выражение X[i] вызывает X.__getitem__(i)
    for i in range(5):
        print(X[i], end=' ',)  # Вызывает __getitem__(X, i) в каждой итерации
    print("\n")
    X = Indexer1()
    print(X[0]) # При индексировании __getitem__
    print(X[1])
    print(X[-1])
    print(X[2:4])# При извлечении среза __getitem__ получает объект среза
"""
Метод __setitem__ присваивания элементу по индексу точно так же обслужи-
вает обе операции – присваивания элементу по индексу и присваивание срезу.
"""
class stepper:
    def __getitem__(self, i):
        return self.data[i]


if __name__ == '__main__':
    X = stepper() # X - это экземпляр класса stepper
    X.data = "Spam"
    print(X[1]) # Индексирование, вызывается __getitem__
    for item in X: # Циклы for вызывают __getitem__
        print(item, end=" ") # Инструкция for индексирует элементы 0..N
    print("p" in X)
    print([c for c in X])
    print(list(map(str.upper, X)))
    (a, b, c, d) = X
    print(a, c, d)
    print(list(X), tuple(X), "".join(X))