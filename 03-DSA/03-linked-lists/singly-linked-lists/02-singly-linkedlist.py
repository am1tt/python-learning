

class singlyNode:

    def __init__(self,val,next=None):
        
        self.val = val
        self.next = next
    
    def __str__(self):
        return str(self.val)



Head = singlyNode(1)
A = singlyNode(3)
B = singlyNode(78)
C = singlyNode(54)


Head.next = A
A.next = B
B.next = C


print(Head.next) ## will print like this though

