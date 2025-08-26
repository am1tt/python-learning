

class Product: 
    def __init__(self,name,price): 
        self.name = name
        self.price = price
    
    def display(self): 
        print(f"Product name : {self.name}")
        print(f"price : {self.price}")


p1 = Product("Monitor",8000)


p1.display()

## used parameterized constructor to 