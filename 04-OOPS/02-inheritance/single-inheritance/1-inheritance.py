

class Person:
    def show_name(self): 
        print("Name : am1tt")
    
class Student(Person): 
    def show_class(self): 
        print("class : python")
    

s = Student()

s.show_name()
s.show_class()

# Student basically now inherits the Person , we can now use Person functions from Student #
# this is single inheritance # 
