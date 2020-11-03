"""
Challenge #6:

Create a function that takes a string, checks if it has the same number of "x"s
and "o"s and returns either True or False.

- Return a boolean value (True or False).
- The string can contain any character.
- When no x and no o are in the string, return True.

Examples:
- XO("ooxx") ➞ True
- XO("xooxx") ➞ False
- XO("ooxXm") ➞ True (Case insensitive)
- XO("zpzpzpp") ➞ True (Returns True if no x and o)
- XO("zzoo") ➞ False
"""
# def XO(txt:str) -> bool:
#     o_counter = 0
#     x_counter = 0

#     for char in txt:
#         if(char.lower() == "o"):
#             o_counter +=1
#         elif (char.lower() == "x"):
#             x_counter += 1
#         else:
#             continue

#     # if(o_counter - x_counter == 0) :
#     #     return True
#     # else:
#     #     return False
#     return o_counter == x_counter

#     # Your code here

def XO(txt: str) -> bool:
    txt = txt.lower()
    return txt.count("x") == txt.count("o")


#Loop over each string
#contains "x"
#contains "o"
# initate x counter
# initaite o counter
# check if counter sum of x counter and o counter = 0
# help("".count)
# dir("")



print(XO("ooxx"))
print(XO("xooxx"))
print(XO("ooxXm"))
print(XO("zpzpzpp"))
print(XO("zzoo"))
