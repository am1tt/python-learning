

class dll:

    def __init__(self,val,next=None,prev=None):
        self.val = val
        self.next = next 
        self.prev = prev
    

    def __str__(self):
        return str(self.val) 


head = tail = dll(1)

def display(head): 
    current = head 

    container = []

    while current: 
        container.append(str(current.val))

        current = current.next 
    
    print(" <-> ".join(container))


def insert_at_beginning(head,tail,val):

    if head is None:
        return head

    new_node = dll(val,next=head)

    head.prev = new_node 

    return new_node,tail 


def insert_at_end(head,tail,val): 
    new_node = dll(val,prev=tail)

    tail.next = new_node 

    return head,new_node

def remove_at_begin(head,tail): 
    if head is None:
        return None, None
    
    if head.next is None:
        return None, None
    
    head = head.next 

    head.prev = None

    return head,tail
    
def remove_at_end(head,tail):
    if tail is None:
        return None
    
    if tail.prev is None:
        return None,None

    tail = tail.prev

    tail.next = None
    return head,tail


head,tail = insert_at_beginning(head,tail,3)

head,tail = insert_at_end(head,tail,8)

# head,tail = remove_at_begin(head,tail)

head,tail = remove_at_end(head,tail)


display(head)

