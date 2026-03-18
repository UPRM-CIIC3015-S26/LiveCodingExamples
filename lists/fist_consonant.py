def first_consonant(word):
    for i in range(len(word)):
        if not word[i] in "AEIOUaeiou":
            return i
    return -1

print (first_consonant("Bienve")) # 0
print (first_consonant("evneiB")) # 1
print (first_consonant("")) # -1
print (first_consonant("AEIOU")) # -1
