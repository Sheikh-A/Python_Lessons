print("**********BLOCKS***")


for i in range(1, 13):
    print("No. {} squared is {} and cubed is {:4}".format(i, i**2, i**3))
print("*" * 80)

# name = input("Please enter name:")
# age = int(input("How old are you, {0}?".format(name)))
# print(age)

# if (age >= 18):
#     print("You can vote!")
#     print("Please put an X in a box")
# elif age > 300:
#     print("Sorry errror")
# else:
#     print("Sorry you cannot vote")

# **********BLOCKS***
# No. 1 squared is 1 and cubed is    1
# No. 2 squared is 4 and cubed is    8
# No. 3 squared is 9 and cubed is   27
# No. 4 squared is 16 and cubed is   64
# No. 5 squared is 25 and cubed is  125
# No. 6 squared is 36 and cubed is  216
# No. 7 squared is 49 and cubed is  343
# No. 8 squared is 64 and cubed is  512
# No. 9 squared is 81 and cubed is  729
# No. 10 squared is 100 and cubed is 1000
# No. 11 squared is 121 and cubed is 1331
# No. 12 squared is 144 and cubed is 1728
# ********************************************************************************
# Please enter name:ali
# How old are you, ali?9
# 9
# Sorry you cannot vote
# ****************************************

print("*" * 40)

answer = 5

print("Please guess a number between 1 and 10: ")
guess = int(input())

# if guess != answer:
#     if(guess < answer):
#         print("Please guess higher")
#     else:
#         print("Please guess lower")
#     guess = int(input())
#     if guess == answer:
#         print("Well done you win")
#     else:
#         print("Sorry wrong")
# else:
#     print("YOU GOT ITS")

while(guess != answer):
    print("Wrong try again")
    guess = int(input())
print("Congrats")

# print("*" * 40)
# print("*" * 40)
# print("*" * 40)
# print("*" * 40)
# print("*" * 40)
# print("*" * 40)
# print("*" * 40)
# print("*" * 40)
