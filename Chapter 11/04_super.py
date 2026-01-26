class Animal:
    def __init__(self):
         print("Constructor of Animal")

    def eat(self):
        print("Animal can eat")

class Dog(Animal):
    def __init__(self):
         print("Constructor of Dog")

    def bark(self):
        print("Dog can bark")

class Puppy(Dog):
    def __init__(self):
         super().__init__() #Call the constructor of the Parent class
         print("Constructor of Puppy")

    def play(self):
        print("Puppy likes to play")

# a=Animal()
# b=Dog()
c=Puppy()