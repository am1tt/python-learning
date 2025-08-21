

class Person:
    def show_person(self): print("a person")



class Student(Person):
    def show_student(self):print(" a student")

class Worker:
    def show_worker(self):print("a worker")

class Intern(Student,Worker):
    def show_intern(self): 
        print("an intern")


i = Intern()

i.show_person()


## single inheritance + multiple inheritance = hybrid 