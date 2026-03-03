word = "Colegio"
# do a while loop that prints each letter individually
# index = 0
# while index < len(word):
#     print(word[index])
#     index += 1

# for letter in word:
#     print(letter)

# # todo range with floats
# for i in range(100, 89, -2):
#     print(i)

# Create a function CheckIn(letter, new_string)
# return true if letter is in new_string, otherwise false
# MUST BE DONE USING FOR LOOP
# def CheckIn(letter, new_string):
#     for l in new_string:
#         if l == letter:
#             return True
#     return False

# print(CheckIn('d', 'abcd'))

# print all the numbers from 0 to 10
# MUST BE DONE WITH A FOR LOOP
# for n in range(11):
#     print(n)

# Create a function CountVowels(new_string)
# return the number of vowels in the string
def CountVowels(new_string):
    out = 0
    for letter in new_string:
        if letter in "aeiou":
            out += 1
    return out

print(CountVowels("aeiou"))
