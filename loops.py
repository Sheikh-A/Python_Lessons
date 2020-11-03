# #for
# #while

# #print 0 to 4

# for x in range(5):
#     print(x)

# for x in range(1,11):
#     print(x)

# for x in range(0,3):
#     print(x)

# for x in range(1, 11, 2):
#     print(x)

# #while loop

# print("WHILES")
# x = 0
# while(x < 5):
#     print(x)
#     x+= 1


# x = 0
# while True:
#     if(x == 5):
#         break
#     print(x)
#     x+= 1

# print("COntinue")
# while (x < 10):
#     x += 1
#     if x % 2 == 0:
#         continue
#     print(x)

"""
Write Python code below to loop through and print out all the odd numbers from the numbers list in the same order they are received. Don't print any numbers that come after 950 in the sequence.
"""

numbers_list = [
  951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 725, 547, 544, 615, 83, 165, 141, 501, 263, 617, 865, 575, 219, 390, 984, 592, 236, 105, 942, 941, 386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 958, 609, 842, 451, 688, 753, 854, 685, 93, 857, 440, 380, 126, 721, 328, 753, 470, 743, 527
]

# YOUR CODE HERE

#print(numbers_list.index(950))

a = []

for num in numbers_list:
    if(numbers_list.index(num) > numbers_list.index(950)):
        break
    else:
        if(num % 2 == 1):
            a.append(num)
            print(num)

print(a)
print(len(a))
