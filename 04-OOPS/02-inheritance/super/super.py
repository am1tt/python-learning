


class A:
    def __init__(self): 
        print("this is : A")

class B(A):
    def __init__(self): 
        super().__init__()
        print("this is B")


b = B()

b.__init__()