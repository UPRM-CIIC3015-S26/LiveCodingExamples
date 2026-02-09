
a = float(input("Please enter quadratic coefficient (a): "))
b = float(input("Please enter linear coefficient (b): "))
c = float(input("Please enter constant coefficient (c): "))

discriminant = b*b - (4*a*c)
if discriminant > 0:
    print("Polynomial has 2 roots")
elif discriminant == 0:
    print("Polynomial has 1 root")
else:
    print("Polynomial has no (real) roots")


