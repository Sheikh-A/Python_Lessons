print("***********BOOLEAN")

x = 10

name = "Ali"

years = [2015,2016,2017,2018,2019,2020]


if(name == 'Ali' and x ==10):
    print("Yay")


year = 2019
if year in years:
    print("2019")
else:
    print("not 2019")


#elif

first = False
second = True

if first:
    print("first")
elif second:
    print("second")
else:
    print("none")


a = [1,2,3]
b = [1,2,3]

print(a==b) #true
print(a is b) #false

print(not True)

print("**********************************PP")

number = 17
second_number = False
first_list = [1,2,3]
second_list = [1,2]
# only change the code above this line

# all of these print statements must print True by only changing the assignment statements above
print(number > 15)
print(first_list)
print(len(second_list) == 2)
print(len(first_list) + len(second_list) == 5)
print(first_list and first_list[0] == 1)
print(not second_number)
