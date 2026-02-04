import math

x1 = int(input("Coordinate x1: "))
y1 = int(input("Coordinate y1: "))
x2 = int(input("Coordinate x2: "))
y2 = int(input("Coordinate y2: "))

result = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

print("Distance:", result)

