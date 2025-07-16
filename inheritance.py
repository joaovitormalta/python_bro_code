class Animal:
    def __init__(self, name):
        self.name = name
        self.is_alive = True

    def eat(self):
        print(f"{self.name} is eating.")

    def sleep(self):
        print(f"{self.name} is sleeping.")

class Dog(Animal):
    def bark(self):
        print(f"{self.name} says Woof!")

class Cat(Animal):
    def meow(self):
        print(f"{self.name} says Meow!")

class Mouse(Animal):
    def squeak(self):
        print(f"{self.name} says Squeak!")

dog = Dog("Buddy")
cat = Cat("Whiskers")
mouse = Mouse("Jerry")

print(dog.name)
dog.eat()
dog.bark()

print(cat.name)
cat.sleep()
cat.meow()

print(mouse.name)
mouse.eat()
mouse.squeak()