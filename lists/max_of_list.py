def max_of_list(my_list):
    maximo = my_list[0]
    for i in range(1,len(my_list)):
        if my_list[i] > maximo:
            maximo = my_list[i]
    return maximo

print(max_of_list([5,7,2,1,9,7,4,6]))

print(max([5,7,2,1,9,7,4,6]))
