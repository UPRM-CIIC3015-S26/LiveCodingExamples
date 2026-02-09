side1 = float(input("Please enter length of first side: "))
side2 = float(input("Please enter length of second side: "))
side3 = float(input("Please enter length of third side: "))

if (side1 == side2) and (side2 == side3):
    print("Triangle is equilateral")
elif side1 == side2 or side2==side3 or side1 == side3:
    print("Triangle is isosceles")
else:
    print("Triangle is scalene")

