
class Person:

    def __init__(self,name,age): 
        self.name = name
        self.age = age 
    
    def show_info(self): 
        print( f"name : {self.name} | age : {self.age}")

class Student(Person): 
    def __init__(self, name, age,grade):
        Person.__init__(self,name,age)

        self.grade = grade
    
    def show_student_grade(self): 
        print( f"| student grade : {self.grade} |")


class Teacher(Person): 
    def __init__(self, name, age,subject):
        Person.__init__(self,name,age)

        self.subject = subject
    
    def show_teacher_subject(self): 
        print( f"| teaches : {self.subject} |") 


s1 = Student("am1tt",21,"A")

t1 = Teacher("smith",40,"python")

s1.show_info()

s1.show_student_grade()

t1.show_info()


t1.show_teacher_subject()

## here Person acts as a parent , and helped reusing the __init__ attr for other child classes
