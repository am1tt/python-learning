

class foo:

    def __init__(self,name,age): ## these are instance attrb 
        self.name = name 
        self.age = age
    

    def myself(self):
        print(f"Hey, myself {self.name} and im {self.age}")



## intializing ob here 

user_1 = foo("amit",21)

user_2 = foo("john",22)



## have to call the method here btw ## 

user_1.myself()