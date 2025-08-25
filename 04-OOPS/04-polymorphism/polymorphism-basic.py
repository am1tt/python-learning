
class Dog: 
    def sound(self): 
        return "bark"

class Cat:
    def sound(self): 
        return "meow"
    
animals = [Dog(),Cat()]



for a in animals: 
    print(a.sound())

## here i same method sound() is used for different purposes ## 