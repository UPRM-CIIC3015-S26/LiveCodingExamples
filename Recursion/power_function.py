def power_x_to_n(x,n):
    # Returns x ** n
    # x ** n = (x * x * x * x * ... * x) * x  n times
    #        = x ** (n-1) * x
    if n == 0:
        return 1
    else:
        return power_x_to_n(x, n-1) * x

print(f"3 ** 3 yields {power_x_to_n(3,3)}")

