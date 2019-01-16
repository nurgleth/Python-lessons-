# Цикл While
a = 1
while a <= 10:
    print("\n List a:", a)
    a += 1
    b = 1
    while b < 5:
        print("List b:", b)
        b += 1




num = input("Enter the number (1, 2, etc):")

while not num.isdigit():
          num = input("Enter the number (1, 2, etc):")
else:
     print("Thanks")