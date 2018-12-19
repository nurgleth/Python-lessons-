# Ветвтление с помощью условного оператора

# ключивое слово else должно располагаться строго под словом if
# синтаксис расмотрим на примерах ниже
# "elif" второе проверочное выражение

num = int(input("Please enter a Number:"))

if num > 100:
    print("Enter a Number > 100")
elif num < 100:
    print("Enter a Number < 100")
else:
    num = 100
    print("Enter a Number = 100!")
if num > 10 and num < 8:
    print("Number = 9")
if num == 0:
    print("Number = 0")




