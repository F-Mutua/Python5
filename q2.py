class Animal:
    def move(self):
        print("Moving")

class Dog(Animal):
    def move(self):
        print("Running")

class Bird(Animal):
    def move(self):
        print("Flying")

class Fish(Animal):
    def move(self):
        print("Swimming")

animals = [Dog(), Bird(), Fish()]
for a in animals:
    a.move()


