

class sll:

    def __init__(self,val,next=None):
        self.val = val
        self.next = next 

    
    def __str__(self): 
        return str(self.val)



head = sll(34)
a = sll(56)
b = sll(89)
c = sll(33)
d = sll(90)

head.next = a 
a.next = b
b.next = c 
c.next = d


def displayAllNodes(head): 

    current = head 

    container = []
    while current:
        container.append(str(current.val))

        current = current.next 

    print(" --> ".join(container))



def searchNode(head,val): 
    current = head

    while current: 
        if current.val == val:
            return True
        
        current = current.next 
    
    return False 



def removeNode(head,node_val): 

    if head is None:
        return head
    
    if head.val == node_val:
        return head.next 
    
    current = head 

    while current and current.next:
        if current.next.val == node_val:
            current.next = current.next.next 
            break 

        current = current.next 
    return head



displayAllNodes(head)

head = removeNode(head,34)

displayAllNodes(head)