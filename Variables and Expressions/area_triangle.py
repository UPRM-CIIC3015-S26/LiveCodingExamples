import math

side_a = float(input("A: "))
side_b = float(input("B: "))
side_c = float(input("C: "))

s = (side_a + side_b + side_c) / 2
area = math.sqrt(s * ((s - side_a) * (s - side_b) * (s - side_c)))

print("Area", area)


