

## consist of non parameterized constructor , does not take arguements except self


class Dev: 
    def __init__(self): 
        self.role = "Cloud dev"
    

    def show(self): 
        print(f"role : {self.role}")


d1 = Dev()

d1.show()

