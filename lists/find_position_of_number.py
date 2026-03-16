def find_position_of_number(number_list, key):
    for i in range(len(number_list)):
        if number_list[i] == key:
            return i
    return -1

print(find_position_of_number([5,7,2,1,9,7,4,6],9))
print(find_position_of_number([5,7,2,1,9,7,4,6],3))
print(find_position_of_number([5,7,2,1,9,7,4,6],7))