# def greet(name, greeting):
#     print(("Hello %s, %s ") % (name, greeting))




# greet("Ali", "today")


# def double(x):
#     return x*2

# x = double(4)

# print(x)


"""
Modify this function to make it return the sum of the arguments a and b.
"""
def sum(a, b):
    return a + b;

# This should print 7
print(sum(2, 5))


"""
Modify this function to use the sum function above to return
the double of the sum of a and b.
"""
def double_the_sum(a, b):
    return 2 * (a+b);

# This should print 14
print(double_the_sum(2, 5))
