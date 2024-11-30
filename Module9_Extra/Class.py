## Classes

"""
Python is an object-oriented language. Just like other languages of similar sort such as Java, they contain what is known as Classes.
Classes are a way to create different functionalities of objects. Classes can be inherited, and can be thought of like a family tree.

Ex. Point class -> Triangle class
Using points on a coordinate plane, a triangle class can make three points to create a triangle object.

Ex2. Animal class -> Dog class
Using the basic features of the animal class, it can be extended/inherited to add more details for a dog object and other possible animals.
"""

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Animal sound"

# Derived class
class Dog(Animal):
    def speak(self):
        return "Woof"

# Create an instance of Dog
dog = Dog("Buddy")
print(dog.name)  # Inherited from Animal
print(dog.speak())  # Overridden method in Dog class