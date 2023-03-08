"""
In this program, we define a parent class called Animal that has a constructor that takes a name parameter and an eat() method. We then define a child class called Dog that inherits from Animal using the syntax class Dog(Animal):. The Dog class also has a bark() method that is specific to Dog instances.

We then create an instance of Dog called my_dog and call the eat() and bark() methods on it. Because Dog inherits from Animal, it has access to the eat() method defined in the Animal class. It also has its own bark() method that is specific to Dog instances.

This program demonstrates how inheritance allows us to define a common set of properties and methods in a parent class that can be reused in child classes. The child classes can then add their own properties and methods on top of the parent class, creating a hierarchy of classes with shared functionality.
"""

class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(self.name + " is eating.")


# Define a child class that inherits from Animal
class Dog(Animal):
    def bark(self):
        print(self.name + " is barking.")


# Create an instance of Dog
my_dog = Dog("Rex")

# Call methods on the instance
my_dog.eat()
my_dog.bark()

