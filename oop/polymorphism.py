"""
In this program, we define an Animal class with a constructor that takes a name parameter and a make_sound() method that is left undefined using the pass statement. This allows us to create subclasses that can override the make_sound() method to produce different sounds.

We then define three subclasses of Animal: Dog, Cat, and Bird. Each of these classes overrides the make_sound() method to produce a different sound.

In the main part of the program, we create a list of animals that includes one instance of each of the subclasses. We then loop through the list and call the make_sound() method on each animal. Because each subclass overrides the make_sound() method, each animal in the list produces a different sound, demonstrating polymorphism.

This program illustrates how polymorphism allows us to write code that can work with objects of different classes in a consistent way. By defining a common interface in the Animal class, we can write code that can operate on any subclass of Animal without needing to know the specific class of each object.
"""
class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        pass


class Dog(Animal):
    def make_sound(self):
        return "Woof!"


class Cat(Animal):
    def make_sound(self):
        return "Meow!"


class Bird(Animal):
    def make_sound(self):
        return "Tweet!"


# Create a list of animals
animals = [Dog("Rex"), Cat("Whiskers"), Bird("Tweety")]

# Make each animal in the list make a sound
for animal in animals:
    print(animal.name + " says " + animal.make_sound())