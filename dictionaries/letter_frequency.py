
def letter_frequency(text):
    result = dict()
    for l in text:
        if l in result:
            result[l] = result[l] + 1
        else:
            result[l] = 1
    return result

print(letter_frequency(('Bienvenido')))

print(letter_frequency("Bienvenido").items())

def most_frequent_letter(text):
    freq_dict = letter_frequency(text)
    max = 0
    max_letter = None
    for l in freq_dict:
        if freq_dict[l] > max:
            max = freq_dict[l]
            max_letter = l
    return max_letter

print(f"Most frequent letter in \'Bienvenidobbb\' is "
      f"{most_frequent_letter('Bienvenidobbb')}")

def are_anagrams(word1, word2):
    d1=letter_frequency(word1)
    d1_sorted=dict(sorted(d1.items()))
    d2=letter_frequency(word2)
    d2_sorted=dict(sorted(d2.items()))
    return d1_sorted == d2_sorted

print(are_anagrams('bienvenido', 'nidobienve'))



