def sum_even_positions(numbers_list):
    suma = 0
    for i in range(len(numbers_list)):
        if i%2 ==0:
            suma += numbers_list[i]
    return suma

print(sum_even_positions([0,1,2,3,4,5,6]))

def sum_evens(numbers_list):
    suma = 0
    for n in numbers_list:
        if n % 2 ==0:
            suma += n
    return suma

print(sum_evens([0,1,2,3,4,5,6]))