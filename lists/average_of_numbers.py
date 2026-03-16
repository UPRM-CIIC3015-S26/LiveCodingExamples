import sum_of_numbers

def average_of_numbers(numbers_list):
    suma = sum_of_numbers.sum_of_numbers(numbers_list)
    avg = suma / len(numbers_list)
    return avg

print(average_of_numbers([0,1,2,3,4,5,6]))
