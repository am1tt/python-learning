

from abc import ABC, abstractmethod



class Animal(ABC): 
    @abstractmethod
    def sound(self): 
        pass


class Dog(Animal): 
    def sound(self): 
        return "bark" 

class Cat(Animal): 
    pass


c = Cat()

print(c.sound())


## the rule is metioned in abstract method to implement sound()
## for the child who inherit the animal , this is how abstract class work 


