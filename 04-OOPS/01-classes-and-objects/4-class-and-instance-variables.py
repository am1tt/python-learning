

class foo: 

    class_variable = "this is class variable"


    def set_detail(self,name,age): 
        self.name = name 
        self.age = age 


## creating objects here l 

person1 = foo()


person1.set_detail("am1tt",21)


print(person1.name)

## class var print 
print(foo.class_variable)

## im accessing the instance variables after creating the object 