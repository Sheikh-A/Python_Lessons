print("***********STRING MANIPULATIONS")

my_string = "Hello, World"

print(len(my_string))

print(my_string.index("e"))
print(my_string.index("ello"))

print(my_string.count("l"))
print(my_string.count("he"))


print(my_string[:1])

print(my_string[1:4])

print(my_string[7:12:2]) #skip

print(my_string[::-1])

print(my_string.upper())
print(my_string.lower())

print(my_string.startswith("H"))
print(my_string.startswith("Help"))

print(my_string.endswith("World"))
print(my_string.endswith("world"))

print(my_string.split(" "))
print(my_string.split(", "))

"""
Modify the "mystery_string" below until all of the print statements print as expected based on the comments above each print call expression.
"""
mystery_string = "Unlockigg potential  regardlessco  aiecimecnace."


print("***************MSTRING")
# Should print out 48
print(len(mystery_string))

# Should print out 5
print(mystery_string.index("k"))

# Should print out 4
print(mystery_string.count("c"))

# Should print out "potential"
print(mystery_string[10:19])

# Should print out "sseldrager"
print(mystery_string[30:20:-1])

# Should print out "Ulcigptnil eadeso icmtne"
print(mystery_string[::2])

# Should print out True
print(mystery_string.startswith("Unlo"))

# Should print out True
print(mystery_string.endswith("stance."))

# Should print out 5
print(len(mystery_string.split()))
