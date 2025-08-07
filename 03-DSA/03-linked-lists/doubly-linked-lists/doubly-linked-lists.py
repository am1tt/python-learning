


class DoublyNode:

    def __init__(self,val,next=None,prev=None):
        self.val = val
        self.next = next
        self.prev = prev 


    def __str__(self):
        return str(self.val)



head = tail = DoublyNode(33)
second = DoublyNode(43)
tail.next = second
second.prev = tail
tail = second




def display(head):
    current = head 
    elements = []

    while current:
        elements.append(str(current.val))

        current = current.next 

    print(" <-> ".join(elements))


display(head)