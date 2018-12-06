# Проверка условий или тернарные оперыторы.
# если истина - возвращаем это - if  (проверочное выражение) else если ложь - возвращаем это
# пример c = a if (a < b ) else b

a = 20
b = 100

# пишем пример, тренеруемся
print("\nVariable a is:" , "supposing true" if (a == 20) else "lie")
print("Variable a is:" , "supposing true" if (a % 5 == 1) else "odd")
# пишем пример, тренеруемся
print("\nVariable b is:" , "supposing true" if (b == 10) else "true")
print("Variable b is:" , "supposing true" if (b % 100 == 0) else "lie")

# выбираем максимальное значение a or b

max = a if ( a > b) else b
print("\n Maximum value:" , max)