import math


class to4ka:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance (self, p2):
        dx = p2.x - self.x
        dy = p2.y - self.y
        return math.sqrt(dx**2+dy**2)

    def __eq__(self, dryga9):
        return self.x == dryga9.x and self.y == dryga9.y

a=to4ka(0,0)
b=to4ka(3,4)

print (a.distance(b))
print(a==b)
print(a==to4ka(0,0))

