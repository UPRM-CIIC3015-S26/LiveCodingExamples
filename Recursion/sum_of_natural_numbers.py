def sum_of_natural_numbers(n):
    # Returns the sum of the first n natural (1..n) numbers
    if  n == 1:
        return 1
    else:
        return sum_of_natural_numbers(n-1) + n

print(sum_of_natural_numbers(5))