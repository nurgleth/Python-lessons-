# примемер "==" равенство
# примемер "!=" неравенство
# примемер ">" большее
# примемер "<" меньше
# примемер ">=" больше либо равно
# примемер "<=" меньше либо равно
# номер кодов  ASCII  верхний регистр от A-Z  имеет  диапазон 65-90
# номер кодов  ASCII  нижний регистр от a-z  имеет  диапазон 97-122

min = 0
max = 1
null = 0
bigline = "A"
lowline = "a"

print("Equality:\t\t" , min , "==", null , min == null)
print("Equality:\t\t" , bigline , "==" , lowline , bigline == lowline)

print("Inequality:\t\t", max , "!=" , min , max != min)
print("Inequality:\t\t", null, "!=" , min , null != min)

print("Great:\t\t\t" , max , ">" , min , max > min)
print("Great:\t\t\t" , bigline, ">" , lowline , bigline > lowline)

print("Lesser:\t\t\t" , min , "<" , max , min < max)
print("Lesser:\t\t\t" , lowline , "<" , bigline , lowline < bigline)

print("More of Equal:\t", min , ">=" , null , min >= null)
print("More of Equal:\t" , min , ">=" , max , min >= max)

print("Less of Equal:\t" , bigline , "<=" , lowline , bigline <= lowline)
print("Less of Equal:\t" , max , "<=" , null , max <= null)