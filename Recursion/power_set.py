def power_set(s):
    if len(s) == 0:
        return [[]]
    subsets_without_first = power_set(s[1:])
    subsets_with_first = []
    for subset in subsets_without_first:
        subsets_with_first.append([s[0]] + subset)
    return subsets_with_first + subsets_without_first

print(power_set([1,2,3]))



