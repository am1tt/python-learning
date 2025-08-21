



class Person: 
    def __init__(self,name,age):
        self.name = name
        self.age = age 
    
    def show_person(self): 
        print("this is a person")


class Student(Person):
    def __init__(self,name,age,grade): 
        super().__init__(name,age)
        self.grade = grade 

    
    def show_student(self):
        print("grade : {self.grade}")


s1 = Student("am1tt",21,"A")

s1.show_person()