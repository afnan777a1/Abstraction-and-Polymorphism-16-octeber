from abc import ABC, abstractmethod

class Absclass(ABC):

    def print(self,x):
        print("Passed value: ", x)

        @abstractmethod
        def task(self):
            print("We are inside Absclass task")

class test_class(Absclass):

    def task(self):
        print("We are inside test_class task")

testObj = test_class()
testObj.task()
testObj.print(100)

o1 = Absclass()
o1.task()