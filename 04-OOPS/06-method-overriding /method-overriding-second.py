


class A: 
    def show(self): 
        print("from class A")


class B(A): 
    def show(self):
        print("from class B")

class C(A): 
    def show(self):
        print("from class C")



class D(B,C):
    pass

d = D()

d.show()