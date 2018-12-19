# Ассоциативные списки

# Словарь или ассоциативный массив(список) контейнер содержащий пары ключ значений
# Обращаться можно по ключу в отличии от списка
# Ключ должен быть уникальным(желательно строкой) в пределах словаря, хотя число не исключается
# Метод keys() возвращает случаным порядке список ключей словаря
# Функция sorted() сортирует список ключей в алфавитном порядке

worker = {"name": "Alex", "age": "28", "prof": "programmer python"}

print("Associative lists:", worker)
# Смотрим профессию
print("\nProf worker:", worker["prof"])
# Выводим смисок всех ключей в ассоциативном списке
print("\nKeys:", worker.keys())
# Удаляем один из ключей
del worker["age"]
# Добавляем ключ в ассоциативный список worker
worker["skill"] = "junior"

print("\nAssociative lists:", worker)
# Проверяем есть ли ключ в списке worker
print("\nSearch:", "skill" in worker)

sorted(worker)
print("\nSorted Keys:", worker)
