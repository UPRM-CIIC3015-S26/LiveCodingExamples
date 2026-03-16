def filter_evens(my_list):
    result = []
    for number in my_list:
        if number % 2 == 0:
            result.append(number)
    return result

print(filter_evens([1,2,3,4,5]))  # [2,4]
print(filter_evens([]))           # []
print(filter_evens([1,3,5]))      # []




