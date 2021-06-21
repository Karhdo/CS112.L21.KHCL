class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
  
def orientation(p1, p2, p3):
    val = (float(p2.y - p1.y) * (p3.x - p2.x)) - (float(p2.x - p1.x) * (p3.y - p2.y))
    if (val > 0):
        return 1
    elif (val < 0):
        return 2
    else:
        return 0

a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]
c = [int(i) for i in input().split()]
p1 = Point(a[0], a[1])
p2 = Point(b[0], b[1])
p3 = Point(c[0], c[1])
  
o = orientation(p1, p2, p3)
  
if (o == 0):
    print("Linear")
elif (o == 1):
    print("Clockwise")
else:
    print("CounterClockwise")