
class MyFirstClass:
    variable = "data"

    def function(self, number):
        print("I am in my function! %d" % number);

a_class = MyFirstClass()
print(a_class.variable)
a_class.function(2)
a_class.function(5)


"""
Below, you'll find a class definition for animals. Create two new animals `cat`
and `dog`. Set `cat` to have a name of "Purrfect", kind of "cat",
and color of "brown". Set `dog` to have a name of "Fido",
kind of "dog", and color of "black".
"""
class Animal:
    name = ""
    kind = ""
    color = ""

    def description(self):
        return "%s is a %s %s." % (self.name, self.color, self.kind)

# Create instances of Animal here and modify the instance attributes
# as described above.

# YOUR CODE HERE


cat = Animal()
cat.name = "Purrfect"
cat.kind = "cat"
cat.color = "brown"


dog = Animal()
dog.name = "Fido"
dog.kind = "dog"
dog.color = "black"

# Should print Purrfect is a brown cat.
print(cat.description())
# Should print Fido is a black dog.
print(dog.description())
