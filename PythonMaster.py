
#STRINGS *****************
#Using Separators

print("*******STRINGS******************************")
number = "9,223;372:036 854,755;807"

separators = number[1::4]
print(separators)

values = "".join(char if char not in separators else " " for char in number).split()
print(values)

print([int(val) for val in values])


## slicing backwards IDIOMS
backwards = number[::-1]
print(letters[-4:]) #last n letters
print(letters[-1:]) #last z
print(letters[:1]) #a
print(letters[0]); #a if empty you get error
