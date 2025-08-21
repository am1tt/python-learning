


class Animal:
    def sound(self): 
        print("animals make different sound")

class Dog(Animal): 
    def bark(self): 
        print("dog : barks")

class Cat(Animal): 
    def meow(self): 
        print("cat : meows")

d = Dog()
d.sound()

d.bark()

# 2  child class inheriting 1 parent class 

## 1 parent class 2 child class 