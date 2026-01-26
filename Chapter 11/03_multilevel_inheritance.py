class Animal:
    def eat(self):
        print("Animal can eat")

class Dog(Animal):
    def bark(self):
        print("Dog can bark")

class Puppy(Dog):
    def play(self):
        print("Puppy likes to play")

# creating object of Puppy class
p = Puppy()
d= Dog()
d.eat()
d.bark()


p.eat()    # from Animal class
p.bark()   # from Dog class
p.play()   # from Puppy class
