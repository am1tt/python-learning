

class Shape:
    def no_of_slides(self): 
        print("shape has many sides")
    
class Rectangle(Shape):
    def no_of_slides(self):
        print("rectangle has 4 sides")



s1 = Shape()
s2 = Rectangle()

s1.no_of_slides()

s2.no_of_slides()

# here child class that is rectangle overide the no_of_slide method

## here we avoid rewriting new methodf 

## changed the method without changing parent class 

## makes the code cleaner and repeatable 

