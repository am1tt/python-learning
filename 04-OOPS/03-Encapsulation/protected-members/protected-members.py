

class Student:

    def __init__(self,name,age): 
        self._name = name
        self._age = age
    
    def show(self): 
        print(f"{self._name} | {self._age}")


class Grad(Student):
    def show_details(self): 
        print(f"grad student : {self._name} | {self._age}")


s1 = Grad("am1tt",21)

s1.show()

s1.show_details()


## altough in java printing an protected | private attribute gives error 
## in python one may do , so yeah thats how protected is for , you cant access the attributes 

print(s1._name)