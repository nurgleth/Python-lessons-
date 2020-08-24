"""
Итераторы: __iter__ и __next__
"""
class Squares:
    def __init__(self, start, stop): # Сохранить состояние при создании
        self.value = start - 1
        self.stop = stop
    def __iter__(self): # Возвращает итератор в iter()
        return self
    def __next__(self): # Возвращает квадрат в каждой итерации
        if self.value == self.stop: # Также вызывается функцией next
            raise StopIteration
        self.value += 1
        return self.value ** 2


if __name__ == "__main__":
    for i in Squares(1, 7):
        print(i)
    X = Squares(1, 5)
    print([n for n in X]) # Получить все элементы
    print([n for n in X]) # Теперь объект пуст
    print([n for n in Squares(1, 5)]) # Создать новый объект итератора
    print(list(Squares(1, 3)))

print("\n")
print([x ** 2 for x in range(1, 6)])

