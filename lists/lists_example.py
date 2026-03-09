# my_list = ['a','b', 'c', 2, False]
#
# for item in my_list:
#     print(item)

# for i in range(len(my_list)):
#     print(my_list[i])

# for num in [1,20,3]:
#     print(num)
# print("no more numbers")

my_list = [1,2,3,4]
print(type(my_list))

# Create a function SumList(my_list), it shall return the total
# sum of all the numbers in the list
# my_list = [1,2,3,4] # 10

# def SumList(my_list):
#     out = 0
#     # for num in my_list:
#     #     out += num
#     i = 0
#     while i < len(my_list):
#         out += my_list[i]
#         i += 1
#     return out
#
# print(SumList([1,1,1]))
# print(SumList([1,2,3]))

# Create a function Sentence(list_words)
# return the list of words in the format of a sentence
# [a, b, c, d] -> "a b c d "
def Sentence(list_words):
    sentence = ""
    for words in list_words:
        sentence += words + " "
    return sentence
    # return ' '.join([words for words in list_words])

print(Sentence(["a", "b", "c", "d"])) # "a b c d "
print(Sentence(["Hello", "World!"])) # "Hello World! "