
class Rectangle: 
    def __init__(self,width=0,height=0):
        if width and height: 
            self.width = width
            self.height = height
        
        elif width: 
            self.width = width
            self.height = width
        else:
            self.width = 0
            self.height = 0
        
    def area(self):
        return self.width * self.height
    
    def display_info(self):
        print(f"width : {self.width}, height : {self.height}, area : {self.area()}")


rec1 = Rectangle(10,20)


rec2 = Rectangle(10) ## only takes width here resulting in square of self

rec3 = Rectangle() # no arg


rec1.display_info()
rec2.display_info()
rec3.display_info()