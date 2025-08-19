

class foo: 
    def __init__(self,name,code):
        self.name = name
        self.code = code 
    

    def __str__(self):
        return f"{self.name} code is : {self.code}"
    

c1 = foo("am1tt","A2006")

print(c1)

## used a __str__ function to reutrn string , usefull for debugs and loggins 

