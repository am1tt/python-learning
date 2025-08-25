

class Shape: 
    def area(self): 
        return "Area formula is not defined"
    
class Circle(Shape): 
    def area(self): 
        return "π * r^2"

class Rectangle(Shape):
    def area(self): 
        return "length * breadth"


shapes = [Circle(),Rectangle(),Shape()]


for s in shapes: 
    print(s.area())


