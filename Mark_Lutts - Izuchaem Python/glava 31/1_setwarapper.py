"""
Дополнительные возможности классов
Расширение типов встраиванием
Использование классов вместо функций позволяет создавать множество независимых объ-
ектов с предопределенными наборами данных и поведением, а не передавать
списки в функции вручную
"""
class Set:
    def __init__(self, value = []): # Конструктор управляет списком
        self.data = []
        self.concat(value)
    def intersect(self, other): # other – любая последовательность self – подразумеваемый объект
        res = []
        for x in self.data:
            if x in other: # Выбрать общие элементы
                res.append(x)
        return Set(res) # Вернуть новый экземпляр Set
    def union(self, other): # other – любая последовательность (метот дополнения нехватающих элементов массива в первый)
        res = self.data[:] # Копировать список
        for x in other: # Добавить элементы из other
            if not x in res:
                res.append(x)
        return Set(res)
    def concat(self, value): # Аргумент value: список, Set
        for x in value: # Удалить дубликаты
            if not x in self.data:
                self.data.append(x)

    def __len__(self): # len(self)
        return len(self.data)

    def __getitem__(self, key): # self[i]
        return self.data[key]

    def __and__(self, other): # self & other
        return self.intersect(other)

    def __or__(self, other): # self | other
        return self.union(other)

    def __repr__(self): # Вывод
        return "Set:" + repr(self.data)

x = Set([1, 3, 5, 7])
print(x.union(Set([1, 4, 7])))
print(x | Set([1 ,4 ,6]))