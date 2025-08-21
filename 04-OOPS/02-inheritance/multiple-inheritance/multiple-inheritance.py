

class A:
    def show_a(self): print("A")

class B:
    def show_b(self):print("b")

class C(A,B):
    def show_c(self):print("c")


c = C()

c.show_b()
c.show_a()
c.show_c()