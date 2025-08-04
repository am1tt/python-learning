


class sLL:

    def __init__(self,val,next=None):
        self.val = val
        self.next = next 
    

    def __str__(self):
        return str(self.val)
    


Head = sLL(54)
A = sLL(5)
B = sLL(78)


Head.next = A
A.next = B


current = Head

while current:
    print(current.val , end=" --> " if current.next else "") 
    current = current.next 