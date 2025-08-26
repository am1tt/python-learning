

class Code:
    def __init__(self):
        self.name = "unknown"
        self.language = "python"
    
    def show(self):
        print(f"name : {self.name}")
        print(f"language : {self.language}")


c = Code() # no params where passed here btw 

c.show()

## non-paremeterized constructor