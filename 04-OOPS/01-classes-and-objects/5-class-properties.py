

class foo: 
    def __init__(self,name): 
        self._name = name
    
    def get_name(self): 
        return self._name 
    
    def set_name(self,value): 
        self._name = value
    
    def del_name(self):
        del self._name
    

    name = property(get_name,set_name,del_name)


## Object here ; 

p1 = foo("am1tt")


print(p1.name)

p1.name = "am1t.sakpal"

print(p1.name)


## created property of name and can resuse it now 

## helps with getter setter , deleter methods 

## help in better attributes control 