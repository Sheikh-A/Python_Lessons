print("This string")

school = "Lambda"

if school == "Lambda":
    print("School is Lambda")

if school == "Lambda":
    print("School is Lambda")


my_int = 3
my_int_2 = int(5.0)

my_float = 2.75
my_float2 = float(4)


my_string = 'hello'
my_string = "hello"

print(my_float)
print(my_float2)
print(my_int)
print(my_int_2)
print(my_string)


#lists
my_list = [1, 2, 3]


print("MY list", my_list[0])

my_list.append(4)
my_list.append(5)
print(my_list)


#iterate through list
for element in my_list:
    print(element)

"""
1. Create a "numbers" list that contains two different integer values and two different
floating point values.

2. Create a "strings" list that contains three different strings.

3. Print the 4th number of your numbers list and the 1st string of your strings list.

4. Iterate through your strings list and print each string.
"""

# YOUR CODE HERE

print("LIST FUNCTIONS")

my_num = [1, 2, 3.5, 6.7]
my_string = ["Hello", "Ali", "Now"]

print(my_num[len(my_num)-1], my_string[0])

##LOOPS
print("loops in Strings")

for element in my_num:
    print(element)

for string in my_string:
    print(string)


# operations
print("************************OPERATIONS*")

a = object()
b = object()

print(a)

a_list = [a] * 5
b_list = [b] * 5

combined_list = a_list + b_list

print(a_list)
print(combined_list)
print(len(combined_list))

"""
1. Assign two different types to the variables "a" and "b".

2. Use basic operators to create a list that contains three instances of "a" and three instances of "b".
"""
# Modify the code below to meet the requirements outlined above
a = "Hello"
b = 20

my_list = [a*3, b*3]

print(my_list)


print("******FORMATTED STRINGS")

name = "Ali"
year = 2020

f_string = "Hello, %s The year is %d" %(name, year)
print(f_string)

p_name = "Bananca"
p_price = 10.00
p_id = 12311231

fmain = "Product Name: %s, Product ID: %d, Price: %.2f" %(p_name, p_price, p_price)

print(fmain)

"""
1. Assign three different types of data to the three variables "a", "b", and "c".

2. Use a format string to inject the data from your three variables into the string.
"""
# Modify the code below to meet the requirements above.
a = "ALi"
b = 10
c = 10.20212

print("My name is %s and I have %d bitcoin and %.4f ethereum" % (a,b,c))
