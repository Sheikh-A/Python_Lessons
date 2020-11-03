# import math

# print(dir(math));

# print(math.factorial(5))

# from math import pow

# print(pow(2,3))


# from math import *
# print(factorial(6))



# sentence = "Every moment is a fresh beginning."

# words = sentence.split()
# word_lengths = []

# # for word in words:
# #     word_lengths.append(len(word))

# #word_lengths = [len(word) for word in words]


# word_lengths = [len(word) for word in words]



# print(word_lengths)

# numbers = [1,2,3,4,5,6,7,8,9,10]

# even_numbers = []

# for number in numbers:
#     if number % 2 == 0:
#         even_numbers.append(number)

# even_numbers_lst_comp = [number for number in numbers if number % 2 == 0]

# print(even_numbers_lst_comp)

# #
# # [<map expression> for <name> in <sequence expression> if <filter expression>]

# """
# Use a list comprehension to create a new list called new_list out of the numbers list. Use the list comprehension to make sure that the new_list only contains positive numbers and make sure they are cast as integers into the new_list.
# """

# print("**************************************")

# numbers = [22.3, -184.4, 57.8, 99.6, -18.2, 84.2, 71.3]

# new_list = [int(num) for num in numbers if num >= 0]
# print(new_list)


"""
Import the "math" module. Then, print an alphabetically sorted list of all the functions available in the "math" module that start with the letters "is".
"""
# YOUR CODE HERE

import math

#print(dir(math))

variable = dir(math)

a = dir(math)
b = []

for words in a:
    if(words.startswith("is")):
        (b.append(words))
        sorted(b)

print(b)
