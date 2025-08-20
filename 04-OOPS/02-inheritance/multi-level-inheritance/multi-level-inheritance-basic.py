

class Grandparent:
    def show_grandparent(self): 
        print(f"grandparent : shares wisdom")


class Parent(Grandparent): 
    def show_parent(self): 
        print(f"shows guidance")

class Child(Parent):
    def show_child(self):
        print(f"learns and grows")



c = Child()


c.show_grandparent()

## here child class is inheriting from both Parent class 
## enabling in accessing and using their methods functions 

## parent class is sub parent and inherting gradparent class 

