def count_vowels(word):
    num_vowels = 0
    for c in word:
        if c in "AEIOUaeiou":
            num_vowels += 1
    return num_vowels

print(count_vowels('Bienvenido'))