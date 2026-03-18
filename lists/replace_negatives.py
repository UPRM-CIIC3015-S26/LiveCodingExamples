def replace_negatives(l, replacement):
    result = []
    for number in l:
        if number < 0:
            result.append(replacement)
        else:
            result.append(number)
    return result

print(replace_negatives([1,2,-3,4,-5], 0)) # [1,2,0,4,0]
print(replace_negatives([1,2,3,4,5], 0))   # [1,2,3,4,5]
print(replace_negatives([], 0))            # []

