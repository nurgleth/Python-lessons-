# оператор "=" пример "a = b" эквивалентная операция а = b
# оператор "+=" пример "a += b" эквивалентная операция a = (a + b)
# оператор "-=" пример "a -= b" эквивалентная операция a = (a - b)
# оператор "*=" пример "a *= b" эквивалентная операция a = (a * b)
# оператор "/=" пример "a /= b" эквивалентная операция a = (a / b)
# оператор "%=" пример "a %= b" эквивалентная операция a = (a % b)
# оператор "//=" пример "a //= b" эквивалентная операция a = (a // b)
# оператор "**=" пример "a **= b" эквивалентная операция a = (a ** b)
a = 15
b = 30
c = 15
print("Assing Values: \t\t\t\t", "a = " , a ,  "\tb = " , b, sep="")
a = c
a += b

print("Add & Assign: \t\t\t\t", "a = ", a , "(15 + 30)", sep="")
a = c
a -= b

print("Substract & Assign: \t\t", "a = ", a , "(15 - 30)", sep="")
a = c
a *= b

print("Multiplication & Assign: \t", "a = " , a , "(15 * 30)", sep="")
a = c
a /= b

print("Division & Assign: \t\t\t", "a = ", a , "(15 / 30)", sep="")
a = c
a %= b

print("Modulus & Assign: \t\t\t", "a = ", a , "(15 % 30)", sep="")
a = c
a //= b

print("Floor division & Assign: \t", "a = ", a , "(15 // 30)", sep="")
a = c
a **= b

print("Exponent & Assign: \t\t\t", "a = ", a , "(15 ** 30)", sep="")









