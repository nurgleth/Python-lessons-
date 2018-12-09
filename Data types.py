# Типы данных и их преобразование

# "int( x )" преобразует "x" в целое число (отбрасывает десятичную часть числа)
# "float( x )" преобразует "х" в число с плавающей точкой (отбрасывает десятичную часть числа)
# "str( x )" преобразует "х" в строковое представление
# "chr( x )" преобразует целое "x" в символ
# "unichr( x )" преобразует целое "х" в символ Юникода (Unicod)
# "ord( x )" преобразует символ "х" в соотвествеющее ему целое число
# "hex( x )" преобразует целое чило "х" в шестанцатеричную строку
#  "oct( x )" преобразует целое "х" в восемеричную строку

a = input("Enter a Number:")
b = input("Another Number ")

sum = a + b
print("\n Data Type sun:" , sum , type(sum))

sum = int(a) + int(b)
print("Data Type sum:" , sum , type(sum))

sum = float (sum)
print("Data Type sum:" , sum , type(sum))

sum = chr ( int(sum))
print("Data Type sum:" , sum, type(sum))
