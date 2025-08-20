


class Person:
    def __init__(self,name,age): 
        self.name = name
        self.age = age
    

    def show_person(self):
        print(f"| name : {self.name} | age : {self.age} |")


class Student(Person): 

    def __init__(self,name,age,grade): 
        Person.__init__(self,name,age)

        self.grade = grade
    

    def show_student_grade(self):
        print(f"| student grade : {self.grade} |")

class GraduateStudent(Student):

    def __init__(self,name,age,grade,thesis): 
        Student.__init__(self,name,age,grade)

        self.thesis = thesis 

    
    def show_thesis(self):
        print(f"| thesis : {self.thesis} |") 


g1 = GraduateStudent("am1tt",21,"A","BCA")


g1.show_person()
g1.show_student_grade()
g1.show_thesis()

## am1tt : as said previously GStudent is inheriting both Student and Person , as the Student inherits the parent Person 
## Making GraduateStudent a child class inheriting both , and easy to use and fill out their attributes and accessing their constructors and methods etc 
