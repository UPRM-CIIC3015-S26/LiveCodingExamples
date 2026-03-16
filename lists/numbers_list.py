
def numbers_list(n):
    """ Return a list of numbers from 0 up to n"""
    result = []
    for i in range(n):
        result.append(i)
    return result

numbers = numbers_list(10)


def reversed_numbers_list(n):
    result = []
    for i in range(n-1,-1,-1):
        result.append(i)
    return result

reversed_numbers = reversed_numbers_list(10)

def reversed_numbers_list_v2(n):
    result = []
    for i in range(n):
        result.insert(0,i)
    return result

reversed_numbers_list_v2 = reversed_numbers_list_v2(10)
print("Done")

