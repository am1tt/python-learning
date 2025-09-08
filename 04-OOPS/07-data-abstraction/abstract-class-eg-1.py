

from abc import ABC , abstractmethod


class Shape(ABC): 
    @abstractmethod
    def info(self): 
        pass




class Rectangle(Shape): 
    def info(self):
        return "4 sides"


r = Rectangle()

print(r.info())