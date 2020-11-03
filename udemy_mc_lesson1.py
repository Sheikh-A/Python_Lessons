#STRINGS *****************
#Using Separators
letters = "abcdefghijklmnopqrstuvwxyz"

backwards = letters[::-1]

#qpo
print(letters[16:13:-1])

#edcba
print(letters[4::-1])

#last 8 letters in reverse
print(letters[:-9:-1])

print(letters[-4:]) #last n letters
print(letters[-1:]) #last z
print(letters[:1]) #a
print(letters[0]); #a if empty you get error

print("*******STRING Operators******************************")

#Sequence
computer_items = ["computer", "monitor","keyboard", "mouse", "mouse mat"]

print(computer_items[1][0]) #m

string1 = "he's "
string2 = "probably "
string3 = "pining "
string4 = "for the "
string5 = "fjords"

print(string1 + string2 + string3 + string4 + string5)
print(string1 , string2 , string3 , string4 , string5)

print("hello " * 5)

day = "Friday"

print("day" in day) #TRue


print("**********STRING REPLACEMENTS")
age = 24
print("My age is " + str(age) + "years")

print("My age is {0} years ".format(age))
print("My age is {0} years ".format(age))

print("There are {0} days in {1} {2} {3} {4} {5}"
    .format(31,"Jan", "Mar", "May", "Jun", "Jul"))

print("There are Jan {2} July {1} Jun {5}".format(1,2,3,4,5,6))

# There are 31 days in Jan Mar May Jun Jul
# There are Jan 3 July 2 Jun 6

print("*****STRING FORMATTING")

for i in range(1,13):
    print("No. {0:2} squared is {1:3} and cubed is {2:4}".format(i, i ** 2, i** 3))

print()

#left align
for i in range(1,13):
    print("No. {0:2} squared is {1:<3} and cubed is {2:<4}".format(i, i ** 2, i** 3))

print()
#center align
for i in range(1,13):
    print("No. {0:2} squared is {1:<3} and cubed is {2:^4}".format(i, i ** 2, i** 3))

print()

print("Pi is approx {0:12}".format(22/7))
print("Pi is approx {0:12f}".format(22/7))
print("Pi is approx {0:12.50f}".format(22/7))
print("Pi is approx {0:52.50f}".format(22/7))
print("Pi is approx {0:62.50f}".format(22/7))
print("Pi is approx {0:72.50f}".format(22/7))

# qpo
# edcba
# zyxwvuts
# wxyz
# z
# a
# a
# *******STRING Operators******************************
# m
# he's probably pining for the fjords
# he's  probably  pining  for the  fjords
# hello hello hello hello hello
# True
# **********STRING REPLACEMENTS
# My age is 24years
# My age is 24 years
# My age is 24 years
# There are 31 days in Jan Mar May Jun Jul
# There are Jan 3 July 2 Jun 6
# *****STRING FORMATTING
# No.  1 squared is   1 and cubed is    1
# No.  2 squared is   4 and cubed is    8
# No.  3 squared is   9 and cubed is   27
# No.  4 squared is  16 and cubed is   64
# No.  5 squared is  25 and cubed is  125
# No.  6 squared is  36 and cubed is  216
# No.  7 squared is  49 and cubed is  343
# No.  8 squared is  64 and cubed is  512
# No.  9 squared is  81 and cubed is  729
# No. 10 squared is 100 and cubed is 1000
# No. 11 squared is 121 and cubed is 1331
# No. 12 squared is 144 and cubed is 1728

# No.  1 squared is 1   and cubed is 1
# No.  2 squared is 4   and cubed is 8
# No.  3 squared is 9   and cubed is 27
# No.  4 squared is 16  and cubed is 64
# No.  5 squared is 25  and cubed is 125
# No.  6 squared is 36  and cubed is 216
# No.  7 squared is 49  and cubed is 343
# No.  8 squared is 64  and cubed is 512
# No.  9 squared is 81  and cubed is 729
# No. 10 squared is 100 and cubed is 1000
# No. 11 squared is 121 and cubed is 1331
# No. 12 squared is 144 and cubed is 1728
# No.  1 squared is 1   and cubed is  1
# No.  2 squared is 4   and cubed is  8
# No.  3 squared is 9   and cubed is  27
# No.  4 squared is 16  and cubed is  64
# No.  5 squared is 25  and cubed is 125
# No.  6 squared is 36  and cubed is 216
# No.  7 squared is 49  and cubed is 343
# No.  8 squared is 64  and cubed is 512
# No.  9 squared is 81  and cubed is 729
# No. 10 squared is 100 and cubed is 1000
# No. 11 squared is 121 and cubed is 1331
# No. 12 squared is 144 and cubed is 1728


print("FSTRINGSS")

age = 24
name = "Ali"
print(name + f"is {age} years old")

print(f"Pi is approx {22/7:12.50f}")
pi = 22/7
print(f"PI is approx {pi:12.50f}")

# FSTRINGSS
# Aliis 24 years old
# Pi is approx 3.14285714285714279370154144999105483293533325195312
# PI is approx 3.14285714285714279370154144999105483293533325195312
