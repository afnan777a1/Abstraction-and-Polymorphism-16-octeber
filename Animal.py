from abc import ABC, abstractmethod

class Animal(ABC):
    def move(self):
        pass

class Human(Animal):
    def move(self):
        print("I can walk and run")

class Snake(Animal):
    def move(self):
        print("I can crawl")


class Dog(Animal):
    def move(self):
        print("I can Bark")

class Lion(Animal):
    def move(self):
        print("I can Roar")

R = Human()
R.move()

H = Snake()
H.move()

F = Dog()
F.move()

K = Lion()
K.move()