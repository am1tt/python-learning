

class Student: 
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def display(self): 
        print(f"name : {self.name}")
        print(f"age : {self.age}")


s1 = Student("am1tt",21)

s1.display()

## Implemented __init__ constructor 