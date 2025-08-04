

## here im going to write a function to display the nodes as well as , searching for the node 



class container:

    def __init__(self,element,next=None):

        self.element = element
        self.next = next 
    

    def __str__(self):
        return str(self.element)

## am1tt : btw str constructor is to return element in str so yeah ## 

Head = container(21)
A  = container(83)
B = container(45)
C = container(89)
D = container(93)
E = container(33)


Head.next = A
A.next = B 
B.next = C 
C.next = D 
D.next = E 



def display(head):
    current = head

    micro_container = []

    while current:
        micro_container.append(str(current.element))
        
        current = current.next

    print(' -> '.join(micro_container) )

## am1tt : i created somewhat of a list to return the container , also joined in using join with the string

def searchElement(head,element):
    current = head 

    while current: 
        if element == current.element: 
            return True
        
        current = current.next 
    
    return False

display(Head)


print(searchElement(Head,89))