def number_exists(number_list, key):
    for number in number_list:
        if number == key:
            return True
    return False

print(number_exists([1,2,3,4,5,6],2))
print(number_exists([1,2,3,4,5,6],9))
